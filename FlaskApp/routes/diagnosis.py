from flask import Blueprint, render_template, request, redirect, url_for, jsonify, session, flash
import time, json

from FlaskApp.utils.json_functions import extract_content
from FlaskApp.utils.doctors import load_all_doctors, load_single_doctor_as_vo
from FlaskApp.utils.session_functions import clear_except_flashes
from FlaskApp.value_objects import LlmRequestVO, PatientVO, DoctorPersonaVO
from FlaskApp.services import api_service
import FlaskApp.utils
import os
from dataclasses import dataclass

diagnosis_bp = Blueprint('diagnosis', __name__)

'''
routes for diagnosis
 - symptoms input
 - diagnosis output
'''

@diagnosis_bp.route('/')
def diagnosis():
    clear_except_flashes()

    default_doctor_id = 1

    doctor_id_from_query = request.args.get('doctor_id', type=int)
    if doctor_id_from_query:
        default_doctor_id = doctor_id_from_query

    doctors = load_all_doctors()

    return render_template('diagnosis.html', doctors=doctors, default_doctor_id=default_doctor_id)

@diagnosis_bp.route('/submit_diagnosis', methods=['POST'])
def submit_diagnosis():
    if not request.form['age'].isdigit():
        flash('Please enter a valid age', 'error')
        return redirect(url_for('diagnosis.diagnosis'))
    elif request.form['symptoms'].strip() == '':
        flash('Please enter a symptom description', 'error')
        return redirect(url_for('diagnosis.diagnosis'))

    session['name'] = request.form['name']
    session['age'] = request.form['age']
    session['gender'] = request.form['gender']
    session['symptoms'] = request.form['symptoms']
    session['family_diseases'] = request.form['family_diseases']
    try:
        session['doctor_id'] = int(request.form['doctors'])
    except ValueError as e:
        flash(f"ValueError: Ungültige Eingabe für 'doctors': {e}", "error")
        return redirect(url_for('diagnosis.diagnosis'))
    except KeyError as e:
        flash(f"KeyError: Der Schlüssel 'doctors' fehlt in der Anfrage: {e}", "error")
        return redirect(url_for('diagnosis.diagnosis'))

    patient_vo = PatientVO(
        name=session.get('name'),
        age=session.get('age'),
        gender=session.get('gender'),
        symptoms=session.get('symptoms'),
        family_medical_history=session.get('family_diseases')
    )


    try:
        doctor_vo = load_single_doctor_as_vo(session.get('doctor_id'))
    except ValueError as e:
        flash("ERROR: " + str(e))
        return redirect('/diagnosis')


    llm_request_vo = LlmRequestVO(patient_vo=patient_vo,
                                  doctor_persona_vo=doctor_vo
                                  )

    try:
        llm_response = api_service.perform_main_llm_call(llm_request_vo)
        print(llm_response)
    except ValueError as e:
        flash("ERROR: " + str(e))
        return redirect('/diagnosis')
    except Exception as e:
        flash("An unexpected error occurred while processing the response. Details: " + str(e))
        return redirect('/diagnosis')

    try:
        session['diagnosis_results'] = extract_content(llm_response)
        print(session.get('diagnosis_results'))
    except KeyError as e:
        flash("KeyError: Missing expected data in the response. Details: " + str(e))
        return redirect('/diagnosis')
    except json.JSONDecodeError as e:
        flash("JSON Error: Failed to parse response content. Details: " + str(e))
        return redirect('/diagnosis')
    except Exception as e:
        flash("An unexpected error occurred while processing the response. Details: " + str(e))
        return redirect('/diagnosis')

    return redirect(url_for('diagnosis.results'))

@diagnosis_bp.route('/results', methods=['GET', 'POST'])
def results():

    diagnosis_result = session.get('diagnosis_results')

    # Liste zur Speicherung von Diagnosen
    diagnosis_list = []

    # Definition der Datenstruktur
    @dataclass
    class Diagnosis:
        diagnose: str
        eintrittswahrscheinlichkeit: str
        empfohlener_facharzt: str

    # Objekte auslesen und der Liste hinzufügen
    for result in diagnosis_result['Ergebnisse']:
        diagnosis_obj = Diagnosis(result['Diagnose'], result['Eintrittswahrscheinlichkeit'], result['EmpfohlenerFacharzt'])
        diagnosis_list.append(diagnosis_obj)

    response_text = None
    error_message = None

    if request.method == 'POST':
        # Prüfen, ob Rückfrage abgesendet
        if 'submit_question' in request.form and request.form['submit_question'] == 'true':
            # Frage des Users ist in user_question abgespeichert
            user_question = request.form.get('user_question', '').strip()

            # Wenn Nutzer nichts gefragt hat aber submitted hat
            if not user_question:
                # Nachricht, die auf der Seite angezeigt wird
                error_message = "Bitte gib eine Rückfrage ein, bevor du sie absendest."
            else:
                # Todo Antworttext basierend auf der Frage setzen => LLM Call
                response_text = f"Vielen Dank für deine Rückfrage: '{user_question}'. Wir kümmern uns darum!"

    # Daten der HTML-Seite übergeben
    return render_template('diagnosisresults.html', diagnosis_list=diagnosis_list, response_text=response_text, error_message=error_message)

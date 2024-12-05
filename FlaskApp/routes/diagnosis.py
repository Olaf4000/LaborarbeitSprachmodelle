from flask import Blueprint, render_template, request, redirect, url_for, jsonify, session, flash
import time, json
from FlaskApp.value_objects import LlmRequestVO, PatientVO, DoctorPersonaVO
from FlaskApp.services import api_service
import os

diagnosis_bp = Blueprint('diagnosis', __name__)

'''
routes for diagnosis
 - symptoms input
 - diagnosis output
'''

@diagnosis_bp.route('/')
def diagnosis():
    clear_except_flashes()

    doctors = load_all_doctors()

    return render_template('diagnosis.html', doctors=doctors)

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
    # session['doctor_id'] = request.form['doctor_id']

    patient_vo = PatientVO(
        name=session.get('name'),
        age=session.get('age'),
        gender=session.get('gender'),
        symptoms=session.get('symptoms'),
        family_medical_history=session.get('family_diseases')
    )

    try:
        print("TryCatch")
        # doctor_vo = load_single_doctor_as_vo(id)
    except ValueError as e:
        flash("ERROR: " + str(e))
        return redirect('/diagnosis')


    llm_request_vo = LlmRequestVO(patient_vo=patient_vo,
                                  doctor_persona_vo=doctor_vo
                                  )
    try:
        session['diagnosis_results'] = api_service.perform_main_llm_call(llm_request_vo)
        print(session.get('diagnosis_results'))
    except ValueError as e:
        flash("ERROR: " + str(e))
        return redirect('/diagnosis')

    return redirect(url_for('diagnosis.results'))

@diagnosis_bp.route('/results')
def results():

    diagnosis_result = session.get('diagnosis_results')

    return render_template('diagnosisresults.html', diagnosis=diagnosis_result)

def clear_except_flashes():
    keys_to_keep = ['_flashes']
    for key in list(session.keys()):
        if key not in keys_to_keep:
            session.pop(key)

def load_all_doctors():
    with open(get_config_path(), 'r', encoding='utf-8') as file:
        doctors = json.load(file)
    return doctors

def load_single_doctor_as_vo(id):
    with open(get_config_path(), 'r', encoding='utf-8') as file:
        doctors = json.load(file)

    for doctor in doctors:
        if doctor["id"] == id:
            DoctorPersonaVO(id=doctor["id"], name=doctor["name"], medical_specialty=doctor["specialization"])
            return doctor
        else:
            return ValueError(f"Could not find doctor. ID: {id}")

def get_config_path():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    config_path = os.path.join(base_dir, '..', 'config', 'doctors.json')

    return config_path
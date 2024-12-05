from flask import Blueprint, render_template, request, redirect, url_for, jsonify, session, flash
import time, json

from FlaskApp.utils.doctors import load_all_doctors, load_single_doctor_as_vo
from FlaskApp.utils.session_functions import clear_except_flashes
from FlaskApp.value_objects import LlmRequestVO, PatientVO, DoctorPersonaVO
from FlaskApp.services import api_service
import FlaskApp.utils
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
    session['doctor_id'] = request.form['doctor']

    patient_vo = PatientVO(
        name=session.get('name'),
        age=session.get('age'),
        gender=session.get('gender'),
        symptoms=session.get('symptoms'),
        family_medical_history=session.get('family_diseases')
    )

    try:
        print("TryCatch")
        doctor_vo = load_single_doctor_as_vo(id)
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
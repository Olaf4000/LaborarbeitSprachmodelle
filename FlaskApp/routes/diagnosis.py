from flask import Blueprint, render_template, request, redirect, url_for, jsonify, session, flash
import time
from FlaskApp.value_objects import LlmRequestVO, PatientVO, DoctorPersonaVO
from FlaskApp.services import api_service

diagnosis_bp = Blueprint('diagnosis', __name__)

'''
routes for diagnosis
 - symptoms input
 - diagnosis output
'''

@diagnosis_bp.route('/')
def diagnosis():

    session.clear()

    return render_template('diagnosis.html', pagemode='home_diagnosis')

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

    patient_vo = PatientVO(
        name=session.get('name'),
        age=session.get('age'),
        gender=session.get('gender'),
        symptoms=session.get('symptoms'),
        family_medical_history=session.get('family_diseases')
    )

    doctor_vo = DoctorPersonaVO(
        name='Lukas Podolski',
        medical_specialty='Allgemeinmedizin'
    )

    llm_request_vo = LlmRequestVO(person_vo=patient_vo,
                                  doctor_person_vo=doctor_vo
                                  )

    session['diagnosis_results'] = api_service.perform_main_llm_call(llm_request_vo)

    return redirect(url_for('diagnosis.results'))

@diagnosis_bp.route('/results')
def results():

    diagnosis_result = session.get('diagnosis_results')

    return render_template('diagnosisresults.html', diagnosis=diagnosis_result)
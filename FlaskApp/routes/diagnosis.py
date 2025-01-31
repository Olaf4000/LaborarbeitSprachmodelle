from flask import Blueprint, render_template, request, redirect, url_for, jsonify, session, flash
import time, json

from FlaskApp.utils.json_functions import extract_content, extract_text
from FlaskApp.utils.doctors import load_all_doctors, load_single_doctor_as_vo
from FlaskApp.utils.session_functions import clear_except_flashes, clear_diagnosis_and_symptoms
from FlaskApp.value_objects import LlmRequestVO, PatientVO, DoctorPersonaVO, LlmFeedbackRequestVO
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
    """
    Displays the diagnosis page with a list of doctors and the selected default doctor.

    Returns:
        Rendered HTML page with doctors and the default doctor ID.
    """
    # Set default doctor ID to 1
    default_doctor_id = 1

    # Check if a doctor_id is passed via query parameters
    doctor_id_from_query = request.args.get('doctor_id', type=int)
    if doctor_id_from_query:
        # Update default doctor ID if a valid one is passed in the query
        default_doctor_id = doctor_id_from_query

    # Load all doctors
    doctors = load_all_doctors()

    # Render the HTML page with the doctors list and the default doctor ID
    return render_template('diagnosis.html', doctors=doctors, default_doctor_id=default_doctor_id)


@diagnosis_bp.route('/clear_session', methods=['GET'])
def clear_session():
    """
    Clears the session (except for flash messages) and redirects to the diagnosis page.

    Returns:
        Redirect to the diagnosis page with the current doctor ID.
    """
    # Clear the session except for flash messages
    clear_except_flashes()

    # Get the doctor_id from the query parameters
    doctor_id = request.args.get('doctor_id')

    # Redirect to the diagnosis page with the current doctor ID
    return redirect(url_for('diagnosis.diagnosis', doctor_id=doctor_id))


@diagnosis_bp.route('/clear_symptoms', methods=['GET'])
def clear_symptoms():
    """
    Clears the diagnosis and symptoms data and redirects to the diagnosis page.

    Returns:
        Redirect to the diagnosis page with the current doctor ID.
    """
    # Clear the diagnosis and symptoms data
    clear_diagnosis_and_symptoms()

    # Get the doctor_id from the query parameters
    doctor_id = request.args.get('doctor_id')

    # Redirect to the diagnosis page with the current doctor ID
    return redirect(url_for('diagnosis.diagnosis', doctor_id=doctor_id))


@diagnosis_bp.route('/submit_diagnosis', methods=['POST'])
def submit_diagnosis():
    """
    Validates and processes the diagnosis form, stores data in the session,
    and triggers the LLM API call for diagnosis.

    Returns:
        Redirects to the diagnosis page with appropriate flash messages
        or to the results page if successful.
    """
    # Validate the age field: Ensure it's a digit
    if not request.form['age'].isdigit():
        flash('Please enter a valid age', 'error')
        return redirect(url_for('diagnosis.diagnosis'))

    # Validate the symptoms field: Ensure it's not empty
    elif request.form['symptoms'].strip() == '':
        flash('Please enter a symptom description', 'error')
        return redirect(url_for('diagnosis.diagnosis'))

    # Store form data in session
    session['name'] = request.form['name']
    session['age'] = request.form['age']
    session['gender'] = request.form['gender']
    session['symptoms'] = request.form['symptoms']
    session['family_diseases'] = request.form['family_diseases']

    # Try to store the doctor ID in the session
    try:
        session['doctor_id'] = int(request.form['doctors'])
    except ValueError as e:
        flash(f"ValueError: Ungültige Eingabe für 'doctors': {e}", "error")
        return redirect(url_for('diagnosis.diagnosis'))
    except KeyError as e:
        flash(f"KeyError: Der Schlüssel 'doctors' fehlt in der Anfrage: {e}", "error")
        return redirect(url_for('diagnosis.diagnosis'))

    # Create a PatientVO object with session data
    patient_vo = PatientVO(
        name=session.get('name'),
        age=session.get('age'),
        gender=session.get('gender'),
        symptoms=session.get('symptoms'),
        family_medical_history=session.get('family_diseases')
    )

    # Try to load the doctor details
    try:
        doctor_vo = load_single_doctor_as_vo(session.get('doctor_id'))
    except ValueError as e:
        flash("ERROR: " + str(e))
        return redirect('/diagnosis')

    # Prepare the LLM request object
    llm_request_vo = LlmRequestVO(patient_vo=patient_vo,
                                  doctor_persona_vo=doctor_vo
                                  )

    # Make the LLM API call and handle errors
    try:
        llm_response = api_service.perform_main_llm_call(llm_request_vo)
        print(llm_response)
    except ValueError as e:
        flash("ERROR: " + str(e))
        return redirect('/diagnosis')
    except Exception as e:
        flash("An unexpected error occurred while processing the response. Details: " + str(e))
        return redirect('/diagnosis')

    # Try to store the diagnosis results in the session
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

    # Redirect to the results page
    return redirect(url_for('diagnosis.results'))

@diagnosis_bp.route('/results', methods=['GET'])
def results():
    """
    Displays the diagnosis results and handles status messages (response and error messages)
    stored in the Flask session.

    Returns:
        Rendered HTML page with diagnosis data, a possible response message, and an error message.
    """
    diagnosis_result = session.get('diagnosis_results')
    diagnosis_list = diagnosis_result.get('Ergebnisse', []) if diagnosis_result else []

    response_text = session.pop('response_text', None)
    error_message = session.pop('error_message', None)

    return render_template('diagnosisresults.html', diagnosis_list=diagnosis_list, response_text=response_text, error_message=error_message)


@diagnosis_bp.route('/post_feedback', methods=['POST'])
def post_feedback():
    """
    Processes user feedback or follow-up questions, generates a response using the LLM API,
    and stores the resulting messages in the Flask session.

    Returns:
        Redirect to the `/results` route with the generated response.
    """
    # Check if a response already exists
    if session.get('response_text'):
        session['error_message'] = "Fehler: Sie können nur eine Folgefrage stellen."
        return redirect(url_for('diagnosis.results'))

    # Check if diagnosis results exist in the session
    if 'diagnosis_results' not in session or session['diagnosis_results'] is None:
        session['error_message'] = "Fehler: Keine Diagnosedaten verfügbar."
        return redirect(url_for('diagnosis.results'))

    # Retrieve user input
    user_question = request.form.get('user_question', '').strip()
    if not user_question:
        session['error_message'] = "Bitte geben Sie eine Folgefrage ein, bevor Sie diese absenden."
        return redirect(url_for('diagnosis.results'))

    # Extract patient and diagnostic data from the session
    try:
        # Create PatientVO from session data
        patient_vo = PatientVO(
            name=session.get('name'),
            age=session.get('age'),
            gender=session.get('gender'),
            symptoms=session.get('symptoms'),
            family_medical_history=session.get('family_diseases')
        )

        # Load doctor persona from session data
        doctor_vo = load_single_doctor_as_vo(session.get('doctor_id'))

        # Get existing diagnosis data from the session
        diagnosis_results = session['diagnosis_results'].get('Ergebnisse', [])
    except KeyError as e:
        session['error_message'] = f"Error: Missing key information for processing feedback. Details: {e}"
        return redirect(url_for('diagnosis.results'))

    # Create the LLM feedback request object
    llm_feedback_request = LlmFeedbackRequestVO(
        patient_vo=patient_vo,
        doctor_persona_vo=doctor_vo,
        diagnosis_results=diagnosis_results,
        user_question=user_question
    )

    # Call the LLM feedback API
    try:
        feedback_response = api_service.perform_feedback_llm_call(llm_feedback_request)

        # Store the response in the session
        session['response_text'] = extract_text(feedback_response)
    except ValueError as e:
        session['error_message'] = f"ValueError: {e}"
        return redirect(url_for('diagnosis.results'))
    except Exception as e:
        session['error_message'] = f"An unexpected error occurred while generating feedback. Details: {e}"
        return redirect(url_for('diagnosis.results'))

    # Redirect back to the results page to display the response
    return redirect(url_for('diagnosis.results'))
import json

from flask import jsonify

from FlaskApp.value_objects import LlmRequestVO, LlmFeedbackRequestVO

import FlaskApp.services.llm_connector_service as conn
import FlaskApp.services.llm_prompt_builder_service as builder

def who_am_i():
    """
    returns a json object containing information about the endpoints used to control the app with only the api
    :return: returns a json object
    """
    return jsonify({
        "message": "Welcome to the apis of the bad doctor!",
        "/diagnosis/" : "this endpoint accepts a LlmRequestVO and returns a Diagnosis object",
        "/simple/" : "passe the provides prompt to the LLM"
    })
    
def perform_simple_llm_call(prompt):
    """
    performs a simple call at the LLM.
    :param prompt:
    :return: response of the llm as a text
    """

    llm_response = conn.send_query("You are a helpful assistant.", prompt).json()
    daten = json.loads(llm_response)

    return daten["Ergebnisse"]


def perform_main_llm_call(llm_request_vo: LlmRequestVO):
    """
    performs the main LLM requests of the app.
    :param llm_request_vo:
    :return: response of the llm as a text
    """

    return conn.send_query(
        builder.build_system_prompt(llm_request_vo.doctor_persona_vo, llm_request_vo.patient_vo.name),
        builder.build_user_prompt(llm_request_vo.patient_vo)
    )


def perform_feedback_llm_call(llm_feedback_request_vo: LlmFeedbackRequestVO):
    """
    Performs a diagnosis feedback LLM call of the app.

    :param llm_feedback_request_vo: Contains all necessary data for feedback LLM processing.
    :return: Response of the LLM as a text.
    """
    # Build the system and user prompts for feedback
    system_prompt = builder.build_feedback_system_prompt(llm_feedback_request_vo.doctor_persona_vo, llm_feedback_request_vo.patient_vo.name)
    user_prompt = builder.build_feedback_user_prompt(
        patient_vo=llm_feedback_request_vo.patient_vo,
        diagnosis_results=llm_feedback_request_vo.diagnosis_results,
        user_question=llm_feedback_request_vo.user_question
    )

    # Send the query and return the response
    return conn.send_query(system_prompt, user_prompt)

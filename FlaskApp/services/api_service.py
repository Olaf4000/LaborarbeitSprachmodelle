from flask import jsonify

from FlaskApp.value_objects import LlmRequestVO

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
    })  #TODO: add description of api endpoints
    
def perform_simple_llm_call(prompt):
    """
    performs a simple call at the LLM.
    :param prompt:
    :return: response of the llm as a text
    """

    return conn.send_query("You are a helpful assistant.", prompt)


def perform_main_llm_call(llm_request_vo: LlmRequestVO):
    """
    performs the main LLM requests of the app.
    :param llm_request_vo:
    :return: response of the llm as a text
    """

    system_content = builder.build_system_prompt(llm_request_vo.doctor_persona_vo)
    user_content = builder.build_user_prompt(llm_request_vo.patient_vo)

    return conn.send_query(system_content, user_content)

"""
Ja Bober das is net wirklich n controller aber wie zum Pferd soll ich dit denne nenne
"""
from FlaskApp.value_objects import LlmRequestVO

from FlaskApp.value_objects.DoctorPersonaVO import DoctorPersonaVO
from FlaskApp.value_objects.PatientVO import PatientVO
from FlaskApp.services.llm_connector_service import send_query


def perform_simple_llm_call(prompt):
    """
    performs a simple call at the LLM.
    :param prompt:
    :return: response of the llm as a text
    """

    return send_query("You are a helpful assistant.", prompt)


def perform_main_llm_call(llm_request_vo: LlmRequestVO):
    """
    performs the main LLM requests of the app.
    :param llm_request_vo:
    :return: response of the llm as a text
    """

    patient_vo: PatientVO = llm_request_vo.patient_vo
    doctor_persona_vo: DoctorPersonaVO = llm_request_vo.doctor_persona_vo

    system_content = "" #TODO: implement dis shit
    user_content = ""

    return send_query(system_content, user_content)


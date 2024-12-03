"""
Ja Bober das is net wirklich n controller aber wie zum Pferd soll ich dit denne nenne
"""
from FlaskApp.value_objects import LlmRequestVO

from FlaskApp.services.llm_connector_service import send_query
from FlaskApp.services.llm_prompt_builder_service import build_user_prompt, build_system_prompt


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

    system_content = build_system_prompt(llm_request_vo.doctor_persona_vo)
    user_content = build_user_prompt(llm_request_vo.patient_vo)

    return send_query(system_content, user_content)


#TODO: refactor class name to meaningful name
"""
Ja Bober das is net wirklich n controller aber wie zum Pferd soll ich dit denne nenne
"""

from FlaskApp.value_objects.general_vos.LlmRequestVO import LlmRequestVO


def perform_main_llm_call(llm_request_vo: LlmRequestVO):
    return llm_request_vo
from flask import jsonify, Blueprint, request

from FlaskApp.value_objects.LlmRequestVO import LlmRequestVO

from services import api_service

api_bp = Blueprint('api', __name__)


@api_bp.route('/', methods=['GET'])
def who_am_i_endpoint():
    """
    Provide Metadata and Usage Information.
    """
    return api_service.who_am_i()



@api_bp.route('/diagnosis/', methods=['POST'])
def perform_main_llm_call_endpoint():
    """
    passes the llm_request_vo to the perform_main_llm_call() of the controller
    :return: perform_main_llm_call()
    """
    try:
        llm_request_vo = request.json
    except: #TODO: fix dis
        return jsonify({
            "error" : "Please provide a valid json object",
        })

    return  api_service.perform_main_llm_call(llm_request_vo)


@api_bp.route('/simple/', methods=['POST'])
def perform_simple_llm_call_endpoint():
    """
    passes the endpoint through to the controller method perform_simple_llm_call()
    :return: controller.perform_simple_llm_call()
    """
    try:
        llm_prompt = request.json['prompt']
    except KeyError:
        return jsonify({
            "error": "No content provided or in the wrong format"
        })

    return api_service.perform_simple_llm_call(llm_prompt)

from flask import jsonify, Blueprint, request

from FlaskApp.api.controller import perform_main_llm_call, perform_simple_llm_call
from FlaskApp.value_objects.LlmRequestVO import LlmRequestVO

api_bp = Blueprint('api', __name__)


@api_bp.route('/', methods=['GET'])
def who_am_i_endpoint():
    """
    returns a json object containing information about the endpoints used to control the app with only the api
    :return: returns a json object
    """
    return jsonify({
        "message": "Welcome to the apis of the bad doctor!",
        "/diagnosis/" : "this endpoint accepts a LlmRequestVO and returns a Diagnosis object",
        "/simple/" : "passe the provides prompt to the LLM"
    })  #TODO: add description of api endpoints


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

    return  perform_main_llm_call(llm_request_vo)


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

    return perform_simple_llm_call(llm_prompt)

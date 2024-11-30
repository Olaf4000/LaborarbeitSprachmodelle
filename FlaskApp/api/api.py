from http.client import responses

from flask import jsonify, Blueprint

from FlaskApp.api.controller import perform_main_llm_call
from FlaskApp.value_objects.general_vos.LlmRequestVO import LlmRequestVO
#import controller

api_bp = Blueprint('api', __name__)


@api_bp.route('/', methods=['GET'])
def who_am_i_endpoint():
    """
    returns a json object containing information about the endpoints used to control the app with only the api
    :return: returns a json object
    """
    return jsonify({
                       "message": "Welcome to the apis of the bad doctor!",
                        "/diagnosis/" : "this endpoint accepts a LlmRequestVO and returns a Diagnosis object"
    })  #TODO: add description of api endpoints


@api_bp.route('/diagnosis/', methods=['POST'])
def perform_main_llm_call_endpoint(llm_request_vo: LlmRequestVO):
    return  perform_main_llm_call(llm_request_vo)

from http.client import responses

from flask import jsonify, Blueprint
from FlaskApp.services.llm_connector_service import send_query

api_bp = Blueprint('api', __name__)


@api_bp.route('/', methods=['GET'])
def who_am_i():
    return jsonify({"message": "Welcome to the apis of the bad doctor! //further explanation//"})


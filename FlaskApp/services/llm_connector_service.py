# Service that handles the connection to the LLM
import os

import requests
from flask.cli import load_dotenv
from requests import Response
from FlaskApp.value_objects.llm_vos.QueryVo import QueryVo

load_dotenv()
llm_uri_base_path = os.getenv("LLM_URI_BASE_PATH")
open_ai_key = os.getenv('LLM_KEY')


def send_query(query: QueryVo) -> Response:
    """
    function passes a query to the defined LLM Base Path (only tested with the openAI API)

    :param query: instance of QueryVo
    :return: response object
    """
    if open_ai_key is None:
        raise ValueError("No OpenAI API key provided")

    headers = {
        "Authorization": "Bearer " + open_ai_key
    }

    data = {
        "model": query.ai_model,
        "messages": [
            {
                "role": "system",
                "content": query.system_role_content
            },
            {
                "role": "user",
                "content": query.user_role_content
            }
        ]
    }

    response = requests.post(llm_uri_base_path, headers=headers, json=data)

    return response

# Service that handles the connection to a LLM
import requests
from flask.cli import load_dotenv

llm_uri_base_path = load_dotenv()


# passas a query straight to the configured LLM
def send_query(query):

    llm_responses = query #TODO: make dis work

    return llm_responses
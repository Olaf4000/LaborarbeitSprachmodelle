import os

class QueryVO:
    """
    This class contains information necessary to make a call on the llm api.
    """
    def __init__(self,system_role_content, user_role_content):
        self.ai_model = os.getenv("LLM_MODEL_NAME")
        self.system_role_content = system_role_content
        self.user_role_content = user_role_content

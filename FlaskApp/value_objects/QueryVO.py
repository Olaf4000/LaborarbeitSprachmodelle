import os

class QueryVO:
    def __init__(self, system_role_content, user_role_content):
        self.ai_model = os.getenv('LLM_MODEL_NAME')
        self.system_role_content = system_role_content
        self.user_role_content = user_role_content

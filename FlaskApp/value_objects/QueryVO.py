import os

class QueryVO:
    def __init__(self, system_role_content, user_role_content):
        self.ai_model = os.getenv('LLM_MODEL_NAME')
        self.system_role_content = system_role_content
        self.user_role_content = user_role_content

    def get_ai_model(self):
        return self.ai_model

    def get_system_role(self):
        return self.system_role_content

    def get_user_role(self):
        return self.user_role_content
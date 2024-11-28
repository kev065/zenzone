import os
from dotenv import load_dotenv

load_dotenv()

class LangGraphIntegration:
    def __init__(self, api_key=os.getenv('LANGGRAPH_API_KEY')):
        self.api_key = api_key

    def generate_response(self, user_input, context):
        pass

    def needs_additional_info(self, response):
        pass

    def update_response(self, response, additional_info):
        pass

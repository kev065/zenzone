import os
from dotenv import load_dotenv

load_dotenv()

class LangChainWorkflow:
    def __init__(self, api_key=os.getenv('LANGCHAIN_API_KEY')):
        self.api_key = api_key

    def execute_workflow(self, user_input):
        pass

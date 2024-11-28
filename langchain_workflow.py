import os
from dotenv import load_dotenv
import requests

load_dotenv()

class LangChainWorkflow:
    def __init__(self, api_key=os.getenv('LANGCHAIN_API_KEY')):
        self.api_key = api_key

    def execute_workflow(self, user_input):
        # API request
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        data = {
            'user_input': user_input
        }
        response = requests.post(f'{self.base_url}/execute_workflow', headers=headers, json=data)

        if response.status_code == 200:
            return response.json().get('workflow_result', 'Workflow executed successfully.')
        else:
            return 'I am sorry, I could not execute the workflow at this time.'

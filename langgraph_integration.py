import os
from dotenv import load_dotenv
import requests

load_dotenv()

class LangGraphIntegration:
    def __init__(self, api_key=os.getenv('LANGGRAPH_API_KEY')):
        self.api_key = api_key

    def generate_response(self, user_input, context):
        # API request
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        data = {
            'user_input': user_input,
            'context': context
        }
        response = requests.post(f'{self.base_url}/generate_response', headers=headers, json=data)

        if response.status_code == 200:
            return response.json().get('response', 'I am here to help you.')
        else:
            return 'I am sorry, I could not generate a response at this time.'

    def needs_additional_info(self, response):
        # logic to determine if additional info is needed
        return 'need more info' in response.lower()

    def update_response(self, response, additional_info):
        # Update the response with additional info
        return f"{response} Here is some additional information: {additional_info}"

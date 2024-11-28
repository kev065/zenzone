import os
from dotenv import load_dotenv
import requests

load_dotenv()

class TavilySearch:
    def __init__(self, api_key=os.getenv('TAVILY_API_KEY')):
        self.api_key = api_key
        self.base_url = 'https://api.tavily.com' 

    def search(self, query):
        # API request
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        data = {
            'query': query
        }
        response = requests.post(f'{self.base_url}/search', headers=headers, json=data)

        if response.status_code == 200:
            return response.json().get('results', 'No results found.')
        else:
            return 'I am sorry, I could not retrieve the information at this time.'

import os
from dotenv import load_dotenv

load_dotenv()

class TavilySearch:
    def __init__(self, api_key=os.getenv('TAVILY_API_KEY')):
        self.api_key = api_key

    def search(self, query):
        pass

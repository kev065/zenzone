from memory import MemoryManager
from langchain_workflow import LangChainWorkflow
from tavily_search import TavilySearch
from langgraph_integration import LangGraphIntegration
import os
from dotenv import load_dotenv

load_dotenv()

class Chatbot:
    def __init__(self):
        self.memory_manager = MemoryManager()
        self.langchain_workflow = LangChainWorkflow()
        self.tavily_search = TavilySearch(api_key=os.getenv('TAVILY_API_KEY'))
        self.langgraph_integration = LangGraphIntegration(api_key=os.getenv('LANGGRAPH_API_KEY'))

    def get_response(self, user_input):
        # Fetch context from memory
        context = self.memory_manager.get_context(user_input)

        response = self.langgraph_integration.generate_response(user_input, context)

        # If response requires additional info, use Tavily for health-related searches
        if self.langgraph_integration.needs_additional_info(response):
            additional_info = self.tavily_search.search(user_input)
            response = self.langgraph_integration.update_response(response, additional_info)

        # Store interaction in memory
        self.memory_manager.store_interaction(user_input, response)

        return response
from memory import MemoryManager
from langchain_workflow import LangChainWorkflow
from tavily_search import TavilySearch
from langgraph_integration import LangGraphIntegration

class Chatbot:
    def __init__(self):
        self.memory_manager = MemoryManager()
        self.langchain_workflow = LangChainWorkflow()
        self.tavily_search = TavilySearch()
        self.langgraph_integration = LangGraphIntegration()

    def get_response(self, user_input):
        # Fetch relevant context from memory
        context = self.memory_manager.get_context(user_input)

        response = self.langgraph_integration.generate_response(user_input, context)

        # If response requires additional info, use Tavily for searches
        if self.langgraph_integration.needs_additional_info(response):
            additional_info = self.tavily_search.search(user_input)
            response = self.langgraph_integration.update_response(response, additional_info)

        # Store the interaction in memory
        self.memory_manager.store_interaction(user_input, response)

        return response
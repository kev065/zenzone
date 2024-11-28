def format_response(response):
    # Format the response for better readability
    return response.capitalize()

def log_interaction(user_input, response):
    # Log the interaction for debugging
    print(f"User: {user_input}")
    print(f"Chatbot: {response}")
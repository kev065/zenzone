import streamlit as st
from chatbot import Chatbot

def main():
    st.title("Wellbeing Chatbot")
    st.write("Welcome! I'm here to support you. How can I assist you today?")

    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = Chatbot()

    user_input = st.text_input("You: ")
    if user_input:
        response = st.session_state.chatbot.get_response(user_input)
        st.text_area("Chatbot:", value=response, height=100)

if __name__ == "__main__":
    main()
    
import streamlit as st
from langchain_openai import ChatOpenAI

# Initialize the chat model
chat_model = ChatOpenAI()

# Title of the application
st.title('Artificial Intelligence Poet')

# Input for the poem topic
content = st.text_input('Please enter the topic of the poem.')

# Define a key for storing the result in the session state
if 'result' not in st.session_state:
    st.session_state.result = None

# Button to request writing a poem
if st.button('Request to write a poem'):
    with st.spinner('Writing poetry...'):
        # Call to the model to generate a poem
        st.session_state.result = chat_model.predict(content + "Write a poem about")

# Display the result if it exists
if st.session_state.result:
    st.write(st.session_state.result)

import streamlit as st
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_openai import ChatOpenAI

# Define a simple callback function to handle output
def handle_output(line):
    # Using Streamlit's session state to append output
    if 'output' not in st.session_state:
        st.session_state.output = ""
    st.session_state.output += line + "\n"

# Create an instance of the callback handler with your function
stdout_callback = StreamingStdOutCallbackHandler(callback=handle_output)

# Initialize the chat model with the callback if supported
chat_model = ChatOpenAI(callbacks=[stdout_callback])

st.title('Artificial Intelligence Poet')

content = st.text_input('Please enter the topic of the poem.')

if st.button('Request to write a poem'):
    with st.spinner('Writing poetry...'):
        # Call to the model to generate a poem
        st.session_state.output = ""  # Resetting the output
        chat_model.predict(content + " Write a poem about")
        st.text_area("Poem Output", value=st.session_state.output, height=300)

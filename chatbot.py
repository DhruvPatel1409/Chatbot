# import os
# import streamlit as st
# from dotenv import load_dotenv
# import google.generativeai as gen_ai

# load_dotenv()

# st.set_page_config(
#     page_title="CHAT WITH GEMINI-PRO !!",
#     page_icon=":brain:",
#     layout="centered"
# )

# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# gen_ai.configure(api_key=GOOGLE_API_KEY)
# model = gen_ai.GenerativeModel('gemini-pro')

# def translate_role_for_streamlit(user_role):
#     if user_role == "model":
#         return "assisstant"
#     else:
#         return user_role

# if "chat_session" not in st.session_state:
#     st.session_state.chat_session = model.start_chat(history=[])

# st.title("🤖 GEMINI PRO - CHATBOT")

# for message in st.session_state.chat_session.history:
#     with st.chat_message(translate_role_for_streamlit(message.role)):
#         st.markdown(message.parts[0].text)

# user_prompt = st.chat_input("Ask Gemini-Pro...")
# if user_prompt:
#     st.chat_message("user").markdown(user_prompt)

#     gemini_response = st.session_state.chat_session.send_message(user_prompt)

#     with st.chat_message("assisstant"):
#         st.markdown(gemini_response.text)

import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

load_dotenv()

st.set_page_config(
    page_title="CHAT WITH GEMINI-PRO !!",
    page_icon=":brain:",
    layout="centered"
)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

try:
    gen_ai.configure(api_key=GOOGLE_API_KEY)
except Exception as e:
    st.error(f"Error configuring GenerativeAI: {e}")
    st.stop()

model = gen_ai.GenerativeModel('gemini-pro')

def translate_role_for_streamlit(user_role):
    return "assistant" if user_role == "model" else user_role

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

st.title("🤖 GEMINI PRO - CHATBOT")

for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

user_prompt = st.chat_input("Ask Gemini-Pro...")
if user_prompt:
    st.chat_message("user").markdown(user_prompt)

    try:
        gemini_response = st.session_state.chat_session.send_message(user_prompt)
        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)
    except Exception as e:
        st.error(f"Error sending message to Gemini-Pro: {e}")


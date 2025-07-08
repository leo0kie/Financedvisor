import streamlit as st
import time
import os
import random

# Initialize and save all session state variables
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
    st.session_state.chat_duration = None
    st.session_state.eval_duration = None

if "consent" not in st.session_state:
    st.session_state.consent = False

if "lowest_chatbot" not in st.session_state:
    st.session_state.lowest_chatbot = None

if "activated_chatbot" not in st.session_state:
    st.session_state.activated_chatbot = None

if "api_key" not in st.session_state:
    st.session_state.api_key = os.environ.get("OPENAI_API_KEY")#st.secrets["OPENAI_API_KEY"]

if "scenario_visible" not in st.session_state:
    st.session_state["scenario_visible"] = False

if "model" not in st.session_state:
    st.session_state["model"] = "meta-llama-3.1-8b-instruct"

if "chatbot1_messages" not in st.session_state:
    st.session_state.chatbot1_messages = []

if "chatbot2_messages" not in st.session_state:
    st.session_state.chatbot2_messages = []

if "chatbot3_messages" not in st.session_state:
    st.session_state.chatbot3_messages = []

if "current_page" not in st.session_state:
    st.session_state.current_page = "None"

if 'current_tab' not in st.session_state:
    st.session_state.current_tab = "Chatting"

if "chat1_disable" not in st.session_state:
    st.session_state.chat1_disable = True

if "chat2_disable" not in st.session_state:
    st.session_state.chat2_disable = True

if "chat3_disable" not in st.session_state:
    st.session_state.chat3_disable = True

if "selected_scenario" not in st.session_state:
    st.session_state.selected_scenario = False

if "evaluation_reminder" not in st.session_state:
    st.session_state.evaluation_reminder = False

if "evaluation_finished" not in st.session_state:
    st.session_state.evaluation_finished = False

# Initialize the pages
st.logo(image="logo.png", size="large")
about_page = st.Page("sites/about.py", title="About this App", icon=":material/more:")
bot1_page = st.Page("sites/bot1.py", title="Chatbot", icon=":material/android:")
bot2_page = st.Page('sites/bot2.py', title='Chatbot', icon=":material/android:")
bot3_page = st.Page('sites/bot3.py', title='Chatbot', icon=":material/android:")
help_page = st.Page('sites/help.py', title='Contact', icon=":material/shield_question:")
consent_page = st.Page("sites/consent.py", title="Consent", icon=":material/approval_delegation:")

if st.session_state["lowest_chatbot"] != None:
    if st.session_state["lowest_chatbot"] == "chatbot_1":
        st.session_state["activated_chatbot"] = bot1_page
    elif st.session_state["lowest_chatbot"] == "chatbot_2":
        st.session_state["activated_chatbot"] = bot2_page
    else:
        st.session_state["activated_chatbot"] = bot3_page
else:
    ran_pages = [bot1_page, bot2_page, bot3_page]
    ran_index = random.randint(0, 2)
    st.session_state["activated_chatbot"] = ran_pages[ran_index]

if st.session_state.consent == True:
    pg = st.navigation(
        {
            "Introduction": [about_page],
            "Testing": [st.session_state.activated_chatbot],
            "Help": [help_page],
        }
    )
else:
    pg = st.navigation(
        [consent_page],
    )

pg.run()
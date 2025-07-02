import streamlit as st
import base
import time

# Initialize and save all session state variables
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
    st.session_state.chat_duration = None
    st.session_state.eval_duration = None

if "lowest_chatbot" not in st.session_state:
    st.session_state.lowest_chatbot = base.get_lowest_usage_chatbot()

if "activated_chatbot" not in st.session_state:
    st.session_state.activated_chatbot = None

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

if st.session_state["lowest_chatbot"] != None:
    if st.session_state["lowest_chatbot"] == "chatbot_1":
        st.session_state["activated_chatbot"] = bot1_page
    elif st.session_state["lowest_chatbot"] == "chatbot_2":
        st.session_state["activated_chatbot"] = bot2_page
    else:
        st.session_state["activated_chatbot"] = bot3_page
else:
    st.session_state["activated_chatbot"] = bot1_page

pg = st.navigation(
    {
        "Introduction": [about_page],
        "Testing": [st.session_state.activated_chatbot],
        "Help": [help_page],
    }
)

pg.run()
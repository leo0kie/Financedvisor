import streamlit as st
from supabase import create_client, Client
import random
import time

# Initialize Supabase client using Streamlit Secrets for security
@st.cache_resource
def intitializeClient():
    SUPABASE_URL = st.secrets["SUPABASE_URL"]
    SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

    return supabase

# Updates the usage counts of the chatbots and selects lowest
@st.cache_data
def get_lowest_usage_chatbot():
    client = intitializeClient()
    response = client.table("chatbot_usage").select("chatbot_name, usage_count").execute()

    if response.data:
        usage_counts = {item["chatbot_name"]: item["usage_count"] for item in response.data}
        if not usage_counts:
            return None

        min_usage = min(usage_counts.values())
        lowest_usage_chatbots = [name for name, count in usage_counts.items() if count == min_usage]
        selected_bot = random.choice(lowest_usage_chatbots)

        usage_count = next((bot['usage_count'] for bot in response.data if bot['chatbot_name'] == selected_bot), None)
        new_count = usage_count + 1
        client.table("chatbot_usage").update({"usage_count": new_count}).eq("chatbot_name", selected_bot).execute()
        return selected_bot
    else:
        return None

#Increments the usage count for a specific chatbot
def increment_usage(chatbot_name):
    client = intitializeClient()
    response = client.table("chatbot_usage").update({"usage_count": client.raw("usage_count + 1")}).eq("chatbot_name", chatbot_name).execute()
    if response.data:
        st.success(f"{chatbot_name} usage incremented!")
    else:
        st.error(f"Error incrementing usage for {chatbot_name}")

# Initialize and save all session state variables
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
    st.session_state.chat_duration = None
    st.session_state.eval_duration = None

if "lowest_chatbot" not in st.session_state:
    st.session_state.lowest_chatbot = get_lowest_usage_chatbot()

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

if "baseline" not in st.session_state:
    st.session_state.baseline = None

if "evaluation_finished" not in st.session_state:
    st.session_state.evaluation_finished = False

# Initialize the pages
st.logo(image="logo.png", size="large")
about_page = st.Page("sites/about.py", title="About this App")
bot1_page = st.Page("sites/bot1.py", title="Chatbot")
bot2_page = st.Page('sites/bot2.py', title='Chatbot')
bot3_page = st.Page('sites/bot3.py', title='Chatbot')
help_page = st.Page('sites/help.py', title='Help')

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
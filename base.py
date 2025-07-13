import streamlit as st
import os
from supabase import create_client, Client
import random

# Get unique session id
def _get_session():
    from streamlit.runtime import get_instance
    from streamlit.runtime.scriptrunner import get_script_run_ctx
    runtime = get_instance()
    session_id = get_script_run_ctx().session_id
    session_info = runtime._session_mgr.get_session_info(session_id)
    if session_info is None:
        raise RuntimeError("Couldn't get your Streamlit Session object.")
    return session_info.session.id

# write evaluation inputs to txt file
def handle_submissions_old(chatbot: str, radio: str, slider1: int, slider2: int, slider3: int, chat_history: list):
    user_id = _get_session()
    filename = f"submission_{user_id}.txt"
    filepath = os.path.join("submissions", filename)
    with open(filepath, "w") as f:
        f.write(f"**{chatbot}** \n\n")
        f.write(f"Time until conversation end: {st.session_state.chat_duration} seconds \n")
        f.write(F"Time until evaluation end: {st.session_state.eval_duration} seconds \n")
        f.write("**Slider Values** \n")
        f.write("Radio: " + radio + "\n")
        f.write("Slider 1: " + str(slider1) + "\n")
        f.write("Slider 2: " + str(slider2) + "\n")
        f.write("Slider 3: " + str(slider3) + "\n\n")
        f.write("Chat History \n")
        for dictionary in chat_history:
            line = "" + dictionary.get("role") + ": \n" + dictionary.get("content") + ""
            f.write(line + "\n")
        f.write("\n\n")

# Initialize Supabase client using Streamlit Secrets for security
@st.cache_resource
def intitializeClient():
    SUPABASE_URL = os.environ.get("SUPABASE_URL")#st.secrets["SUPABASE_URL"]
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY")#st.secrets["SUPABASE_KEY"]
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

    return supabase

# Updates the usage counts of the chatbots and selects lowest
#@st.cache_data
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

def generate_evaluation(chat: str):    
    eval_form = st.form(chat)
    
    eval_form.markdown(":one: **Will you, as Taylor, follow the chatbot's given recommendation?**")
    radio = eval_form.radio('Make a decision', options=["Yes", "No"])
    eval_form.write("")
    eval_form.markdown(":two: **To you personally, how confident sounded the chatbot based on the way it responded?**")
    slider1 = eval_form.slider('Choose your perceived confidence value by adjusting the slider', 1, 10, key=3, help="1 referring to 'very uncertain', 10 meaning 'very confident'")
    eval_form.write("")
    eval_form.markdown(""":three: **How strongly do you agree with the statement: "The chatbot's answers seemed correct/valid"?**""")
    slider2 = eval_form.slider('Choose your level of agreement by adjusting the slider', 1, 10, key=4, help="1 referring to 'completely disagree', 10 meaning 'fully agree'") 
    eval_form.write("")
    eval_form.markdown(":four: **Do you personally have experience in the domain of stocks and trading?**")
    slider3 = eval_form.slider('Choose your experience/knowledge level by adjusting the slider', 1, 10, key=5, help="1 referring to 'no experience at all', 10 meaning 'long-term experience about markets, stocks and investing'")
    eval_form.write("")
    eval_form.markdown(":five: **What is your gender?**")
    select = eval_form.selectbox("Select one item", ("Female", "Male", "Non-binary", "Prefer not to say"), index=None, placeholder="none")
    eval_form.write("")
    eval_form.markdown(":six: **What is your age?**")
    number = eval_form.number_input(label="Enter your age numerically", min_value=0, max_value=99, step=1, value=None, placeholder="NaN")
    eval_form.write("")
    
    return eval_form, radio, slider1, slider2, slider3, select, number

def handle_submissions(chatbot: str, radio: str, slider1: int, slider2: int, slider3: int, select: str, number: int, chat_history: list):
    user_id = _get_session()
    submission = {
        "user_id": user_id,
        "chatbot_used": chatbot,
        "duration_until_conversation_end": st.session_state.chat_duration,
        "duration_until_evaluation_end": st.session_state.eval_duration,
        "follows_advice": radio,
        "confidence_value": slider1,
        "correctness_value": slider2,
        "experience_level": slider3,
        "gender": select,
        "age": number,
        "chat_history": chat_history
    }

    client = intitializeClient()
    response = client.table("evaluation_submissions").insert(submission).execute()
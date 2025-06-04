import streamlit as st
import os
from app import intitializeClient

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

def handle_submissions(chatbot: str, radio: str, slider1: int, slider2: int, slider3: int, chat_history: list):
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
        "chat_history": chat_history
    }

    client = intitializeClient()
    response = client.table("evaluation_submissions").insert(submission).execute()
    print(response)
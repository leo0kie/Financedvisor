import streamlit as st

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
def handle_submissions(chatbot: str, radio: str, slider1: int, slider2: int, slider3: int, chat_history: list):
    user_id = _get_session()
    f = open(f".data/{user_id}.txt", "a")
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
    f.close() 
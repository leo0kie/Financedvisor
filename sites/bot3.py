import streamlit as st
import time
import chat
import base
import texts as tx
import os

st.title('Financedvisor 3')

st.header('Chat with me!', divider=True)

if st.session_state["selected_scenario"] == False:
    st.warning(f"{tx.chat_warning}", icon="⚠️")
else:
    st.write(f"""Your concerns:   
        :point_right: {tx.scenario_one}  
        :point_right: {tx.scenario_two}  
        """)

if st.session_state.chat3_disable == False or st.session_state.selected_scenario == False:
    tab = st.segmented_control(
        "Tab options",
        ["Chatting"],
        selection_mode="single",
        default="Chatting",
        disabled=True,
        label_visibility="collapsed"
        )

elif st.session_state.chat3_disable == True and st.session_state.selected_scenario == True:
    tab = st.segmented_control(
        "Tab options",
        ["Chatting", "Evaluation"],
        selection_mode="single",
        default=st.session_state.current_tab,
        label_visibility="collapsed"
    )

chat_bot3 = chat.Chat(st.session_state.api_key, "https://chat-ai.academiccloud.de/v1", "meta-llama-3.1-8b-instruct", st.session_state.chatbot3_messages, "third_person_hedging")

#def check_page_change():
#    chat_bot3.check_page_change(app.bot3_page.url_path)
#check_page_change()
def end_button_clicked():
    st.session_state.chat3_disable = True
    if st.session_state.chat_duration is None:
        st.session_state.chat_duration = round(time.time() - st.session_state.start_time)
    st.session_state.current_tab = "Evaluation"

def eval_button_clicked():
    st.session_state.evaluation_finished = True
    if st.session_state.eval_duration is None:
        st.session_state.eval_duration = round(time.time() - st.session_state.start_time)

if tab == "Chatting":
    st.session_state.current_tab = "Chatting"
    for message in st.session_state.chatbot3_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Check for user input and streams conversation
    user_query = st.chat_input("How can I help you?", disabled=st.session_state.chat3_disable)
    if user_query:
        with st.chat_message("user"):
            st.markdown(user_query)
        chat_bot3.chat_history.append({"role": "user", "content": user_query})
        stream = chat_bot3.generateStream(chat_bot3.chat_history)

        with st.chat_message("assistant"):
            response = st.write_stream(stream)
        chat_bot3.chat_history.append({"role": "assistant", "content": response})

    if len(st.session_state.chatbot3_messages) > 0:
        end_button = st.button("End conversation", on_click=end_button_clicked, disabled=st.session_state.chat3_disable)
        if st.session_state.evaluation_reminder == False:
            time.sleep(3)
            st.toast("When you're finished, don\'t forget to click the 'End Conversation' button which has now appeared!", icon=":material/star:")
            time.sleep(4)
            st.toast("This will lead you to the evaluation page where you can rate the chatbot!", icon=":material/star:")
            st.session_state.evaluation_reminder = True

else:
    eval_form = st.form("chat3")
    with eval_form:
        st.markdown(":one: **Will you, as Taylor, follow the chatbot's given recommendation?**")
        radio = st.radio('Make a decision', options=["Yes", "No"])
        st.write("")
        st.markdown(":two: **To you personally, how confident sounded the chatbot based on the way it responded?**")
        slider1 = st.slider('Choose your perceived confidence value by adjusting the slider', 1, 10, key=3, help="1 referring to 'very uncertain', 10 meaning 'very confident'")
        st.write("")
        st.markdown(""":three: **How strongly do you agree with the statement: "The chatbot's answers can be perceived as correct/valid"?**""")
        slider2 = st.slider('Choose your level of agreement by adjusting the slider', 1, 10, key=4, help="1 referring to 'completely disagree', 10 meaning 'fully agree'") 
        st.write("")
        st.markdown(":four: **Do you personally have experience in the domain of stocks and trading?**")
        slider3 = st.slider('Choose your experience/knowledge level by adjusting the slider', 1, 10, key=5, help="1 referring to 'no experience at all', 10 meaning 'long-term experience about markets, stocks and investing'")

        submitted = st.form_submit_button("Submit", on_click=eval_button_clicked, disabled=st.session_state.evaluation_finished)

    if submitted:
        base.handle_submissions("ChatBot 3", radio, slider1, slider2, slider3, chat_bot3.chat_history)
        st.success("Evaluation has sucessfully been committed. Thank you for your attendance!", icon="✅")
        st.balloons()
        st.info("You can close this window now.", icon="👋")
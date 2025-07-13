import streamlit as st
import time
import chat
import base
import texts as tx

st.title('Financedvisor 3')

st.header('Chat with me!', divider=True)

with st.expander("Your Portfolio", icon="🧾"):
            a, b = st.columns(2)
            c, d = st.columns(2)
            e, f = st.columns(2)
            st.markdown("_Time stamp_: 2025-04-30")
            a.metric("U.S. Broad Market ETF (VTI)", "602,80$", "-3.8%", border=True)
            b.metric("U.S. Domestic Manufacturing ETF (IYJ)", "298,92$", "-1.20%", border=True)
            
            c.metric("Defensive Dividend Stock (PG)", "226,52$", "-4.25%", border=True)
            d.metric("Tech Stock (APPLE)", "225,35$", "-18.00%", border=True)
            
            e.metric("European Equity ETF (VGK)", "151,18$", "+16.87%", border=True)

            st.markdown("\n\n")
            st.markdown(f"**Please notice**: :small[{tx.advisor}]")

if st.session_state["selected_scenario"] == False:
    st.warning(f"{tx.chat_warning}", icon="⚠️")
else:
    st.write(f"""Your concerns:   
        :point_right: {tx.scenario_one}  
        :point_right: {tx.scenario_two}  
        :information_source: {tx.eval_reminder}
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

def end_button_clicked():
    st.session_state.chat3_disable = True
    if st.session_state.chat_duration is None:
        st.session_state.chat_duration = round(time.time() - st.session_state.start_time)
    st.session_state.current_tab = "Evaluation"

def eval_button_clicked():
    if st.session_state.eval_duration is None:
        st.session_state.eval_duration = round(time.time() - st.session_state.start_time)

if tab == "Chatting":
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
    eval, radio, slider1, slider2, slider3, select, number = base.generate_evaluation("chat3")

    submitted = eval.form_submit_button("Submit", disabled=st.session_state.evaluation_finished)

    if submitted and not st.session_state.evaluation_finished:
        has_error = False

        if select == None or number == None:
            st.error("Gender or Age cannot be none.")
            has_error = True
        
        if not has_error:
            eval_button_clicked()
            base.handle_submissions("ChatBot 3", radio, slider1, slider2, slider3, select, number, chat_bot3.chat_history)
            st.session_state.evaluation_finished = True
            st.success("Evaluation has sucessfully been committed. Thank you for your attendance!", icon="✅")
            st.balloons()
            st.info("You can close this window now.", icon="👋")
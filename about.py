import streamlit as st
import chat
import texts as tx


def select_scenario():
    st.session_state["selected_scenario"] = True
    initiate = chat.Chat(st.secrets["OPENAI_API_KEY"], st.secrets["BASE_URL"], st.secrets["MODEL_NAME"])
    baseline = initiate.create_baseline_answer()
    answer = baseline.choices[0].message.content
    st.session_state["baseline"] = answer
    print(answer)
    st.session_state.chat1_disable = False
    st.session_state.chat2_disable = False
    st.session_state.chat3_disable = False

#FRONTEND
st.title('Confidence of Chatbots')

with st.container(border=False):
    st.header('Are you hedging?', divider=True)

    st.markdown(f":small[{tx.about_info}]")
    if st.session_state["scenario_visible"] == False:
        if st.button(label="Jump to the scenario!", key="act"):

            st.session_state["scenario_visible"] = True

if st.session_state["scenario_visible"] == True:
    with st.container(border=True):
        st.subheader('🎓 Taylor - a student`s investment plans', divider=True)

        st.markdown(f":small[{tx.introduction_one}]")

        with st.expander("Taylor's Portfolio", icon="🧾"):
            a, b = st.columns(2)
            c, d = st.columns(2)
            e, f = st.columns(2)
            st.markdown("_Time stamp_: 2025-04-30")
            a.metric("U.S. Broad Market ETF", "278,80$", "-3.8%", border=True)
            b.metric("U.S. Domestic Manufacturing ETF", "131,92$", "-1.20%", border=True)
            
            c.metric("Defensive Dividend Stock", "160,52$", "-4.25%", border=True)
            d.metric("Tech Stock", "205,35$", "-18.00%", border=True)
            
            e.metric("European Equity ETF", "74,18$", "+16.87%", border=True)

            st.markdown("\n\n")
            st.markdown(f"**Please notice**: :small[{tx.advisor}]")

    with st.container(border=True):
        st.markdown(f":small[{tx.introduction_two}] \n")

    with st.container(border=True):
        st.image("background.jpeg")
        st.markdown(f"👾:small[{tx.vestra}] \n")

    with st.container(border=True):
        st.subheader("💼 Your Move:")
        st.markdown(":small[Now it's your turn! As Taylor, you want to find out how to proceed with the assets in your stock portfolio. Expand the boxes below to find out more!]")
        with st.expander(label="Portfolio Strategy & Diversification:", icon="📈"):
            st.caption(f'You think about selling the tech stocks right now because they have been consistenly losing value. Is that a good idea?')

        with st.expander(label="Tariff & Trade Policy Impact", icon="🌍"):
            st.caption(f'You are wondering if you should increase investments in the European Equity ETF as it seems less impacted by U.S. protectionist policies.')

        st.markdown(":small[To clarify those questions, click on the button below to activate the virtual assistant and ask him for advice!]")
        if st.button(label="Start the virtual financial assistant..", key=tx.scenario_two):
            with st.spinner("Loading information...", show_time=True):
                select_scenario()
            st.success("_Financedvisor_ is now ready!\n\n:small[Under the **Testing** section in the sidebar on the left of the page click on **Chatbot**.]", icon="✅")

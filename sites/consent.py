import streamlit as st
import base

st.title("Informed Consent of Study Participation")

st.markdown("""
You are invited to participate in the online study "Chatbot Finance Advisor". The study is conducted by Leonard Kiefner and supervised by Laura Spillner from the University of Bremen. The study with estimated 50 participants takes place in the period from 2025-07-14 to 2025-07-28. Please note:  
""")
st.markdown("""<ul><li>Your participation is entirely voluntary and can be discontinued or withdrawn at any time</li><li>One session of the online study will last ca. 9 minutes</li><li>You have no direct benefit from participating in the study, but you support our work and help to advance research in this area</li><li>With the submission of the evaluation at the end of the session, we will log your input</li><li>Input data are treated with confidentiality and will be fully anonymized stored, evaluated and possibly made publicly available as raw data sets so that no conclusions can be drawn about individual persons</li></ul>""", unsafe_allow_html=True)
st.markdown("The alternative to participation in this study is to choose not to participate. If you have any questions, concerns, or complaints about the informed consent process of this research study or your rights as a human research subject, please contact Laura Spillner. Please read the following information carefully and take the time you need.")
st.header("1. Purpose and Goal of this Research")
st.markdown("""
This study is conducted as part of a bachelor thesis. Its goal is to study users' trust in a chatbot giving advice on financial decisions. Your participation will help us achieve this research goal. The results of this research may be presented at scientific or professional meetings or published in scientific proceedings and journals.
""")

st.header("2. Study Participation")
st.markdown("""
Your participation in this online study is entirely voluntary and can be discontinued or withdrawn at any time. You can refuse to answer any questions or continue with the study at any time if you feel uncomfortable in any way. You can discontinue or withdraw your participation at any time without giving a reason. However, we reserve the right to exclude you from the study (e.g., with invalid trials or if continuing the study could have a negative impact on your well-being or the equipment). Repeated participation in the study is not permitted.
""")

st.header("3. Study Procedure")
st.markdown("""After confirming this informed consent the procedure is as follows:  
""")
st.markdown("""<ol>
    <li>Reading the introduction to this application</li>
    <li>Getting familiar with the case example presented</li>
    <li>Interacting with the chatbot</li>
    <li>Evaluating the experience with the chatbot's interaction</li>
</ol>""", unsafe_allow_html=True)

st.header("4. Risks and Benefits")
st.markdown("""
In the online study you will not be exposed to any immediate risk or danger. As with all computer systems on which data is processed, despite security measures, there is a small risk of data leakage. You have no direct benefit from participating in the study, but you support our work and help to advance research in this area.
""")

st.header("5. Risks and Benefits")
st.markdown("""
    In this study, personal data are collected for our research. The use of personal or subject-related information is governed by the European Union (EU) General Data Protection Regulation (GDPR) and will be treated in accordance with the GDPR. This means that you can view, correct, restrict processing, and delete the data collected in this study. Only with your agreement, 
    we will log your input. We plan to publish the results of this and other research studies in academic articles or other media. Your data will not be retained for longer than necessary or until you contact researchers to have your data destroyed or deleted. Access to the raw data of the study 
    during the analysis is encrypted, password-protected and only accessible to the authors, colleagues, and researchers collaborating on this research. As part of the research, the data will be fully anonymized and then be made available to the general public, whereas no conclusions can be drawn about individual persons. Once the material has been made publicly available, 
    the distribution of the data can no longer be revoked. Since no contact details (e.g. emails) are collected, the researchers cannot inform the participants about further details of the study or about a possible breach of data.
""")

st.header("6. Identification of Investigators")
st.markdown("""
If you have any questions or concerns about the research, please feel free to contact:  
""")
a, b = st.columns(2)
a.markdown("""
Researcher  
Leonard Kiefner (leo_kie@uni-bremen.de)  
University of Bremen                
""")
b.markdown("""
Principal investigator  
Laura Spillner  
laura.spillner@uni-bremen.de  
University of Bremen  
Bibliothekstraße 1  
28359 Bremen, Germany
""")
st.write("\n\n")
if st.button("With clicking this button I agree to the Consent Information and want to participate in this study"):
    st.session_state.consent = True
    st.session_state.lowest_chatbot = base.get_lowest_usage_chatbot()
    st.rerun(scope="app")
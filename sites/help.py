import streamlit as st

st.header('Help & Contact')

with st.container(border=True):
    st.write(""":small[If you have any questions, face an issue with the app or want to drop a feedback, please don\'t hesitate to contact us via e-mail.]  
             """)
    a, b = st.columns(2)
    a.markdown("""Researcher  
               Leonard Kiefner // _leo_kie@uni-bremen.de_""")
    b.markdown("""Supervisor  
              Laura Spillner // _laura.spillner@uni-bremen.de_""")




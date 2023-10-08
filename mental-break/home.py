# Importing the Streamlit library
import streamlit as st
import streamlit_authenticator as stauth
from google.cloud import language_v1

# Page configurations
st.set_page_config(
    page_title="Home"
)

# Streamlit app title
st.title("Mental Breakdown")
st.write("A journaling web application that analyzes your daily journal entries and provides feedback on ways to improve the next day.")


# Login
authenticator = stauth.Authenticate(
    dict(st.secrets['credentials']).copy(),
    st.secrets['cookie']['name'],
    st.secrets['cookie']['key'],
    st.secrets['cookie']['expiry_days'],
    st.secrets['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')
# print(name, authentication_status, username)
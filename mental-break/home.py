import streamlit as st
import streamlit_authenticator as stauth
import journal

import yaml
from yaml.loader import SafeLoader


# Page configurations
st.set_page_config(
    page_title="Mental Breakdown",
    page_icon="📘",
)

# Login
def login():
    with open('./config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )

    firstname, authentication_status, username = authenticator.login('Login', 'main')
    print(firstname, authentication_status, username)

    if authentication_status == False:
        st.error("Username/passwords is incorrect")
    elif authentication_status == None:
        st.warning("Please enter your username and password")
    else:
        journal.show(firstname, username)

# Home
def home():
    st.title("Mental Breakdown")
    st.write("A journaling web application that analyzes your daily journal entries and provides feedback on ways to improve the next day.")
    login()

# Main
home()
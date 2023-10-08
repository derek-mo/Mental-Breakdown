import journal
import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from streamlit_extras.app_logo import add_logo

# Page configurations
st.set_page_config(
    page_title="Mental Breakdown",
    page_icon="📘",
)

# Add the page logo
add_logo("./assets/logo.png", 180)

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

    name, authentication_status, username = authenticator.login('Login', 'main')
    print(name, authentication_status, username)

    if authentication_status == False:
        st.error("Username/passwords is incorrect")
    elif authentication_status == None:
        st.warning("Please enter your username and password")
    else:
        authenticator.logout('Logout', 'sidebar')
        journal.show(name, username)

# Home
def home():
    st.title("📖 Mental Breakdown 📖")
    st.write("A journaling web application that analyzes your daily journal entries and provides feedback on ways to improve the next day.")
    login()

# Main
home()
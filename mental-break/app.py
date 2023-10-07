# Importing the Streamlit library
import streamlit as st
import streamlit_authenticator as stauth

from pymongo.mongo_client import MongoClient

# Streamlit app title
st.title('Mental Breakdown')



# Login

# Connect to your MongoDB database
# client = MongoClient("mongodb+srv://<username>:<password>@<cluster-url>/<dbname>?retryWrites=true&w=majority")
# db = client['<dbname>']

# # Define a collection for user data
# users = db['users']

authenticator = stauth.Authenticate(
    dict(st.secrets['credentials']).copy(),
    st.secrets['cookie']['name'],
    st.secrets['cookie']['key'],
    st.secrets['cookie']['expiry_days'],
    st.secrets['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')
print(name, authentication_status, username)

# Authenticating users
if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main', key='unique_key')
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
    print("test")
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')

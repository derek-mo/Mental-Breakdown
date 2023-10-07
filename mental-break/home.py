# Importing the Streamlit library
import streamlit as st

# Streamlit app title
st.title('Personalized Greeting App')

# User input for name
name = st.text_input('What is your name?')

# Displaying personalized greeting
if name:
    st.write(f'Hello, {name}! Welcome to the Streamlit app.')
else:
    st.write('Enter your name above.')

# Adding an image to the app
st.image('./assets/happyhappyhappycat.gif', caption='HAPPYHAPPYHAPPY', use_column_width=True)

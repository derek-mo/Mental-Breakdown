# Importing the Streamlit library
import streamlit as st

# Streamlit app title
st.title('Personalized Greeting App')

# User input for name
name = st.text_input('Enter your name')

# Displaying personalized greeting
if name:
    st.write(f'Hello, {name}! Welcome to the Streamlit app.')
else:
    st.write('Enter your name above.')

# Adding an image to the app
st.image('https://placekitten.com/300/200', caption='Random Kitten', use_column_width=True)

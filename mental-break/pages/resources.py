# Importing the Streamlit library
import streamlit as st
from streamlit_card import card

# Resources Page
st.title(" :mending_heart: HealthyHub :mending_heart:")
st.write("## this is a link [we love](https://google.com)")

col1, col2 = st.columns(2)

with col1:
    try:
        card(
            title="Asians Mental Health Collective",
            text="Some description",
            image="http://placekitten.com/300/250",
            url="https://www.google.com",
        )
    except:
        st.write("")

    try:
        card(
            title="happyhapu",
            text="Some description",
            image="http://placekitten.com/300/250",
            url="https://www.google.com",
        )
    except:
        st.write("")


with col2:
    try:
        card(
            title="I love your mom",
            text="Some description",
            image="http://placekitten.com/300/250",
            url="https://www.google.com",
        )
    except:
        st.write("")

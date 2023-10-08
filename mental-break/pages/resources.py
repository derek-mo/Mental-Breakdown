# Importing the Streamlit library
import streamlit as st
from streamlit_card import card

# Resources Page
st.title(" :exclamation: :mending_heart: HealthyHub :mending_heart: :exclamation:")
st.write("### Mental Health in the Asian Community")
st.write("In the Asian community, mental health is a topic that is often overlooked and"
         " ignored. Let's break down some of the obstacles in the community below!")

culture_expand = st.expander("Cultural Background and Stigmas")
culture_expand.write("- In a lot of Asian families, there is a fear of being outcast, with family reputation and community expectations on the line.")
culture_expand.write("- Creates a false perception of the Asian American identity as a monolith")

mmm_expand = st.expander("The Model Minority Myth")
mmm_expand.write("- The Model Minority Myth pressures Asians and Asian Americans to succeed, often at the cost of their mental well-being.")
mmm_expand.write("- Creates a false perception of the Asian American identity as a monolith")


res_expand = st.expander("Underutilizing Services")
res_expand.write("- There is a large language barrier for mental health services. 32.6% of AAPI Americans are not fluent in English.")
res_expand.write("- Lack of Asian therapists")


st.divider()
st.write("### Resources for the Asian community:")
col1, col2 = st.columns(2)

with col1:
    try:
        card(
            title="Asian Mental Health Collective",
            text="Some description",
            image="http://placekitten.com/300/250",
            url="https://www.asianmhc.org/",
        )
    except:
        st.write()

    try:
        card(
            title="Asians Do Therapy",
            text="Some description",
            image="http://placekitten.com/300/250",
            url="https://asiansdotherapy.com/",
        )
    except:
        st.write()
    
    try:
        card(
            title="NQAPIA",
            text="National Queer Asian Pacific Islander Alliance",
            image="http://placekitten.com/300/250",
            url="https://www.nqapia.org/",
        )
    except:
        st.write()

    try:
        card(
            title="Asian American Psychological Association",
            text="National Queer Asian Pacific Islander Alliance",
            image="http://placekitten.com/300/250",
            url="https://aapaonline.org/",
        )
    except:
        st.write()



with col2:
    try:
        card(
            title="NAAPIMHA",
            text="The National Asian American Pacific Islander Mental Health Association",
            image="http://placekitten.com/300/250",
            url="https://www.google.com",
        )
    except:
        st.write()
    
    try:
        card(
            title="Asian American Health Initiative",
            text="helloooooo",
            image="http://placekitten.com/300/250",
            url="https://aahiinfo.org/",
        )
    except:
        st.write()

    try:
        card(
            title="South Asian Therapists Directory",
            text="helloooooo",
            image="http://placekitten.com/300/250",
            url="https://southasiantherapists.org/",
        )
    except:
        st.write()

    try:
        card(
            title="Asians for Mental Health",
            text="helloooooo",
            image="http://placekitten.com/300/250",
            url="https://asiansformentalhealth.com/",
        )
    except:
        st.write()


source_expand = st.expander("Sources and References")
source_expand.write("[1] insert link")
source_expand.write("[2] insert link")
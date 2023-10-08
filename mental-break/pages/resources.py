# Importing the Streamlit library
import streamlit as st
from streamlit_card import card
from streamlit_extras.app_logo import add_logo

# Add the page logo
add_logo("./assets/logo.png", 180)

# Resources Page
st.title(" :exclamation: :adhesive_bandage: :heart: HealthyHub :heart: :adhesive_bandage: :exclamation:")
st.write("### Mental Health in the Asian Community")
st.write("###### In the Asian community, mental health is a topic that is often overlooked and"
         " ignored. In fact, Asians are 60% less likely to receive treatment for mental health issues.")
st.write("Let's *break down* some of the obstacles in the community below!")

culture_expand = st.expander("Cultural Background and Stigmas")
culture_expand.write("- In a lot of Asian families, there is a fear of being outcast, with family reputation and community expectations on the line.")
culture_expand.write("- Culturally, there are a lot of traditional beliefs that mental health is taboo that"
                     " is caused by lack of harmony or evil spirits.")
culture_expand.write("- There is importance placed on the family unit, which are disrupted by mental health problems.")
culture_expand.write("- A difference in upbringing by the older and younger generations create a disparity in their understanding of mental health.")

mmm_expand = st.expander("The Model Minority Myth")
mmm_expand.write("- The Model Minority Myth pressures Asians and Asian Americans to succeed, often at the cost of their mental well-being.")
mmm_expand.write("- Perception that the Model Minority is a positive stereotype, when it is actually damaging.")
mmm_expand.write("- Creates a false perception of the Asian American identity as a monolith. There are many different Asian cultures, and"
                 " placing everyone in one bucket is misleading, every background has different experiences.")


res_expand = st.expander("Underutilizing Services")
res_expand.write("- There is a large language barrier for mental health services. 32.6% of AAPI Americans are not fluent in English.")
res_expand.write("- The lack of Asian therapists and service providers make existing resources less appealing and harder to access.")
res_expand.write("- Financial strain can be a deterrant from accessing resources, and many Asians prefer informal solutions"
                 " to their mental health issues rather than seeking professional help.")


st.divider()
st.write("### Resources for the Asian community:")
col1, col2 = st.columns(2)

with col1:
    try:
        card(
            title="Asian Mental Health Collective",
            text="",
            image="https://www.asianmhc.org/wp-content/uploads/2021/07/amhc-featured.jpg",
            url="https://www.asianmhc.org/",
        )
    except:
        st.write()

    try:
        card(
            title="Asians Do Therapy",
            text="",
            image="https://img1.wsimg.com/isteam/ip/6e6678f3-0bb5-413f-9e82-4fcda60eda54/Asians_Do_Therapy_Podcast.jpg/:/cr=t:0%25,l:0%25,w:100%25,h:100%25",
            url="https://asiansdotherapy.com/",
        )
    except:
        st.write()
    
    try:
        card(
            title="NQAPIA",
            text="National Queer Asian Pacific Islander Alliance",
            image="https://www.guidestar.org/ViewEdoc.aspx?eDocId=5146286&approved=True",
            url="https://www.nqapia.org/",
        )
    except:
        st.write()

    try:
        card(
            title="AAPA",
            text="Asian American Psychological Association",
            image="https://media.licdn.com/dms/image/C4E0BAQFs31J2hFxg-g/company-logo_200_200/0/1625615091168?e=2147483647&v=beta&t=602EgI7kQkLCrTxC4iO8H6SrlZO_2ype8DyCkGA36qs",
            url="https://aapaonline.org/",
        )
    except:
        st.write()



with col2:
    try:
        card(
            title="NAAPIMHA",
            text="The National Asian American Pacific Islander Mental Health Association",
            image="data:image/jpeg;base64,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",
            url="https://www.naapimha.org/",
        )
    except:
        st.write()
    
    try:
        card(
            title="AAHI",
            text="Asian American Health Initiative",
            image="https://pbs.twimg.com/profile_images/604034355120340992/6EnSQB2l_400x400.png",
            url="https://aahiinfo.org/",
        )
    except:
        st.write()

    try:
        card(
            title="South Asian Therapists Directory",
            text="",
            image="data:image/png;base64,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",
            url="https://southasiantherapists.org/",
        )
    except:
        st.write()

    try:
        card(
            title="Asians for Mental Health",
            text="",
            image="https://res.cloudinary.com/djchuang-com/images/f_auto,q_auto/v1651345871/asianmh/asianmh.png?_i=AA",
            url="https://asiansformentalhealth.com/",
        )
    except:
        st.write()

st.divider()


source_expand = st.expander("Sources and References")
source_expand.write("[1] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1071736/ ")
source_expand.write("[2] https://www.nami.org/Your-Journey/Identity-and-Cultural-Dimensions/Asian-American-and-Pacific-Islander#:~:text=AAPIs%20have%20the%20lowest%20help,health%20care%20and%20quality%20treatment ")
source_expand.write("[3] https://ph.ucla.edu/news/news-item/2021/may/confronting-mental-health-barriers-asian-american-and-pacific-islander   ")
source_expand.write("[4] https://www.thechicagoschool.edu/insight/from-the-magazine/the-model-minority-myth/")
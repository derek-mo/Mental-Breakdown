import streamlit as st
import pandas as pd
from google.cloud import language_v1
from streamlit_extras.chart_container import chart_container
from streamlit_extras.chart_container import _get_random_data

# configure the page
st.set_page_config(
    page_title="Journal",
    page_icon="📘",
)


# contains all data for an entry
class Entry:
    title = ""
    content = ""
    score = 0

    def __init__(self, title, content, score):
        self.title = title
        self.content = content
        self.score = score

def calcScore(content : str):
    # ======== GOOGLE CLOUD NLP ========
    # Instantiates a client
    client = language_v1.LanguageServiceClient()

    # The text to analyze
    text = content
    document = language_v1.types.Document(
        content=text, type_=language_v1.types.Document.Type.PLAIN_TEXT
    )

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(
        request={"document": document}
    ).document_sentiment

    sentiment.score = round(sentiment.score, 2)

    if sentiment.score > 0.7:
        print("Extremely Positive")
    elif sentiment.score > 0.4:
        print("Average")
    elif sentiment.score > 0.2:
        print("Poor")
    print(f"Text: {text}")
    print(f"Sentiment: {sentiment.score}")

    return round(sentiment.score, 2)

st.write("# Welcome to Your Journal! 👋")
tab1, tab2, tab3 = st.tabs(["New", "History", "Analysis"])

# creates a list of entries in session state if it doesn't exist
if ("entries" not in st.session_state):
    st.session_state["entries"] = []

# contains the code for the "New" tab
with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.write("### New Entry")
        # create text boxes for the entry
        title = st.text_input("Write a title.")
        content = st.text_area("Write the content.")
        # checks if the submitted entry is valid
        if st.button("Submit"):
            if(len(title) == 0 and len(content) == 0):
                st.error("Invalid entry.")
            elif(len(title) == 0):
                st.error("Invalid title.")
            elif(len(content) == 0):
                st.error("Invalid content")
            else:
                st.session_state["entries"].append(Entry(title, content, calcScore(content)))
                st.success("Saved new entry.")
                st.success(st.session_state["entries"][len(st.session_state["entries"])- 1].score)
                

# contains the code for the "History" tab
with tab2:
    st.write("### History")
    # writes the data from the entries
    for i in range(len(st.session_state["entries"]) - 1, -1, -1):
        entry = st.session_state["entries"][i]
        with st.expander("**" + entry.title + "**"):
            st.write(entry.content)
            col1, col2, NULL = st.columns([1, 1, 3])
            with col1:
                st.button("Modify", key = "modify" + str(i))
                # TODO: Modify Button Functionality
                st.button("Delete", key = "delete" + str(i))
                # TODO: Delete Button Functionality

with tab3:
    st.write("### Analysis")

    chart_data = _get_random_data()

    with chart_container(chart_data):
        st.write("Here's a cool chart")
        st.area_chart(chart_data)
        
# st.session_state 

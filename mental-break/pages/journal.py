import streamlit as st
from google.cloud import language_v1
from streamlit_extras.chart_container import chart_container

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

    if sentiment.score > 0.7:
        print("Extremely Positive")
    elif sentiment.score > 0.4:
        print("Average")
    elif sentiment.score > 0.2:
        print("Poor")
    print(f"Text: {text}")
    print(f"Sentiment: {sentiment.score}")

    return sentiment.score


st.write("# Welcome to Your Journal! 👋")
tab1, tab2 = st.tabs(["New", "History"])
entries = []

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
                entries.append(Entry(title, content, calcScore(content)))
                st.success("Saved new entry.")
                st.success(entries[0].score)
                

# contains the code for the "History" tab
with tab2:
    st.write("### History")
    # writes the data from the entries
    for entry in entries:
        st.write(entry.title)
        st.write(entry.content)

import streamlit as st
from google.cloud import language_v1

# configure the page
st.set_page_config(
    page_title="Journal",
    page_icon="📘",
)


# contains all data for an entry
class Entry:
    title = ""
    content = ""

    def __init__(self, title, content):
        self.title = title
        self.content = content


def analyze(entry: Entry):
    # ======== GOOGLE CLOUD NLP ========
    # Instantiates a client
    client = language_v1.LanguageServiceClient()

    # The text to analyze
    text = entry.content
    document = language_v1.types.Document(
        content=text, type_=language_v1.types.Document.Type.PLAIN_TEXT
    )

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(
        request={"document": document}
    ).document_sentiment

    print(f"Text: {text}")
    print(f"Sentiment: {sentiment.score}")

st.write("# Welcome to Your Journal! 👋")
tab1, tab2 = st.tabs(["New", "History"])

# creates a list of entries in session state if it doesn't exist
if ("entries" not in st.session_state):
    st.session_state["entries"] = []

# contains the code for the "New" tab
with tab1:
    st.write("### New Entry")
    # create text boxes for the entry
    title = st.text_input("Write a title.")
    content = st.text_area("Write the content.")
    # checks if the submitted entry is valid
    if (st.button("Submit")):
        if (len(title) == 0 and len(content) == 0):
            st.error("Invalid entry.")
        elif (len(title) == 0):
            st.error("Invalid title.")
        elif (len(content) == 0):
            st.error("Invalid content")
        else:
            st.session_state["entries"].append(Entry(title, content))
            st.success("Saved new entry.")

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
        
# st.session_state 

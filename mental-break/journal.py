import certifi
import datetime
import streamlit as st
import pandas as pd
from google.cloud import language_v1
from streamlit_extras.chart_container import chart_container
from streamlit_extras.tags import tagger_component
from pymongo import MongoClient

def show(name, curr_user):
    # Establish MongoDB connection
    client = MongoClient('mongodb+srv://jareuhmee:mental@cluster0.d5dlehi.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp', tlsCAFile=certifi.where())
    db = client['mental_breakdown']
    collection = db['entries']

    # Contains all data for an entry
    class Entry:
        username = ""
        title = ""
        content = ""
        score = 0
        rank = ""
        color = ""
        time = ""

        def __init__(self, username, title, content, score):
            self.username = username
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

        return round(sentiment.score, 2)

    st.write(f"## Welcome {name} to Your Journal! 👋")
    tab1, tab2, tab3 = st.tabs(["New", "History", "Analysis"])

    # Contains the code for the "New" tab
    with tab1:
        st.write("### New Entry")

        # Create text boxes for the entry
        title = st.text_input("Write a title.")
        content = st.text_area("Write the content.")

        # Checks if the submitted entry is valid
        if (st.button("Submit")):
            if (len(title) == 0 and len(content) == 0):
                st.error("Invalid entry.")
            elif (len(title) == 0):
                st.error("Invalid title.")
            elif (len(content) == 0):
                st.error("Invalid content")
            else:
                # Create new instance of entry object
                new_entry = Entry(curr_user, title, content, calcScore(content))

                if new_entry.score > 0.6:
                    new_entry.rank = "Great"
                    new_entry.color = "green"
                elif new_entry.score > 0.2:
                    new_entry.rank = "Okay"
                    new_entry.color = "bluegreen"
                elif new_entry.score > -0.2:
                    new_entry.rank = "Neutral"
                    new_entry.color = "orange"
                elif new_entry.score > -0.6:
                    new_entry.rank = "Bad"
                    new_entry.color = "red"
                else:
                    new_entry.rank = "Awful"
                    new_entry.color = "yellow"

                # Get the current time
                time = datetime.datetime.now()
                time = time.strftime("%B %d, %Y %I:%M %p")
                new_entry.time = time

                # Insert the new entry
                collection.insert_one(vars(new_entry))
                st.success("Saved new entry.")
                

    # Contains the code for the "History" tab
    with tab2:
        st.write("### History")

        # Writes the data from the entries
        entries = collection.find({"username": curr_user})

        for i, entry in enumerate(entries):
            with st.expander("**" + entry["title"] + "**"):
                st.write("*" + entry["time"] + "*")
                st.write(entry["content"])

                col1, col2 = st.columns([1, 5])
                with col1:
                    if st.button("Delete", key = "delete" + str(i)):
                        collection.delete_one(entry)
                        st.rerun()
                with col2:
                    tagger_component("Day: ", [entry["rank"]], color_name=[entry["color"]])

    # Contains the code for the "Analysis" tab
    with tab3:
        st.write("### Analysis")

        data = {"Column 1": []}

        entries = collection.find({"username": curr_user})
        for i, entry in enumerate(entries):
            data["Column 1"].append(entry["score"])

        chart_data = pd.DataFrame(data)

        with chart_container(chart_data):
            st.area_chart(chart_data)
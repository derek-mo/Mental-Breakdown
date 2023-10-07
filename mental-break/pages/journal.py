import streamlit as st

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
                entries.append(Entry(title, content))
                st.success("Saved new entry.")

# contains the code for the "History" tab
with tab2:
    st.write("### History")
    # writes the data from the entries
    for entry in entries:
        st.write(entry.title)
        st.write(entry.content)
import streamlit as st
import resume_processor
# Set page title
st.set_page_config(page_title="My Streamlit App", layout="wide")


hide_streamlit_style = """
<style>
/* Hide the Streamlit menu (MainMenu) */
#MainMenu {visibility: hidden;}

/* Hide the footer */
footer {visibility: hidden;}

/* Hide the deploy button (more aggressive approach) */
[data-testid="stAppDeployButton"] {display: none !important;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Settings"])

# Load the selected page
if page == "Home":
    resume_processor.show()
# elif page == "About":
#     about.show()
# elif page == "Settings":
#     settings.show()
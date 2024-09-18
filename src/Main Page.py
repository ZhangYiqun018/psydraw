import streamlit as st
from PIL import Image

st.set_page_config(page_title="PsychePal", page_icon=":house::evergreen_tree:", layout="wide")

st.sidebar.image("assets/logo2.png", use_column_width=True)
st.sidebar.write("# House-Tree-Person Projective Drawing Test")
st.sidebar.write("## Introduction")
st.sidebar.write("""The House-Tree-Person Projective Drawing Test (HTP) can be administered to children, adolescents, and adults, ages 3 and up. The primary purpose of the HTP is to measure aspects of a person’s personality through interpretation of drawings and responses to questions. It provides clinically useful information about a person’s psychological, emotional, and mental health status.
""")

st.write("This is a simple web application that uses the House-Tree-Person test to analyze an image.")

st.image("assets/main_page.jpeg", use_column_width=True)
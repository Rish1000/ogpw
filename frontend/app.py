import streamlit as st
import requests

st.title("OGPW Frontend")
st.write("Click the button to talk to the FastAPI backend!")

if st.button("Run Analysis"):
    response = requests.get("http://localhost:8000/analyze")
    st.write(response.json())

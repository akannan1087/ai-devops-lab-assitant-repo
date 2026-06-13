import streamlit as st
from agent import ask_agent

st.set_page_config(page_title="CoachDevOps AI Lab Assistant")

st.title("Coach AK AI Lab Assistant")
st.write("Ask DevOps, CI/CD, Kubernetes, Cloud, and DevSecOps questions.")

option = st.selectbox(
    "Choose a lab assistant mode",
    [
        "Generate CI/CD Pipeline",
        "Explain Pipeline",
        "Troubleshoot Error",
        "Improve Pipeline with DevSecOps"
    ]
)

user_input = st.text_area("Enter your requirement, pipeline, or error message")

if st.button("Ask AI Assistant"):
    if user_input.strip():
        prompt = f"""
Mode: {option}

Student request:
{user_input}
"""
        answer = ask_agent(prompt)
        st.write(answer)
    else:
        st.warning("Please enter a question or requirement.")

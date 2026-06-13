import streamlit as st
from agent import ask_agent

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="CoachDevOps AI Lab",
    page_icon="🚀",
    layout="wide"
)

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🚀 CoachDevOps AI Lab")
st.subheader("Your Personal DevOps, Cloud, DevSecOps & SRE Learning Assistant")

st.markdown("""
Welcome to **CoachDevOps AI Lab**.

Learn faster with AI-powered guidance on:

✅ CI/CD Pipelines  
✅ Jenkins & GitLab CI/CD  
✅ GitHub Actions & Azure DevOps  
✅ Docker & Kubernetes  
✅ Terraform & Infrastructure as Code  
✅ DevSecOps & Security Scanning  
✅ Site Reliability Engineering (SRE)  
✅ AWS & Azure Cloud  
✅ DevOps Interview Preparation  

---
""")

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:
    st.header("📚 CoachDevOps AI Lab")

    st.info("""
    Learn and practice:

    • DevOps
    • CI/CD
    • Kubernetes
    • Terraform
    • Cloud
    • DevSecOps
    • SRE
    """)

    st.markdown("---")

    st.markdown("### 💡 Sample Questions")

    st.markdown("""
    - Create a GitLab CI/CD pipeline
    - Explain this Jenkinsfile
    - Fix a Maven build error
    - Troubleshoot Kubernetes pod crash
    - Generate Terraform code
    - Prepare for DevOps interview
    """)

# --------------------------------------------------
# Assistant Mode
# --------------------------------------------------

option = st.selectbox(
    "🎯 Select Learning Mode",
    [
        "Generate CI/CD Pipeline",
        "Explain CI/CD Pipeline",
        "Troubleshoot Build Failure",
        "Kubernetes Troubleshooter",
        "Terraform Generator",
        "DevSecOps Advisor",
        "SRE Incident Analysis",
        "DevOps Interview Coach"
    ]
)

# --------------------------------------------------
# User Input
# --------------------------------------------------

user_input = st.text_area(
    "💬 Enter your requirement, code, YAML, log, or error message",
    height=250,
    placeholder="""
Examples:

Create a GitLab CI/CD pipeline for a Java Maven application.

Explain this Jenkinsfile.

Why is my Kubernetes pod crashing?

Fix this Maven build error:
maven-war-plugin:2.2
Cannot access defaults field of Properties

Generate Terraform code for an EC2 instance.

Prepare me for a DevOps interview.
"""
)

# --------------------------------------------------
# Submit Button
# --------------------------------------------------

if st.button("🚀 Ask CoachDevOps AI", use_container_width=True):

    if user_input.strip():

        with st.spinner("Analyzing your request..."):

            prompt = f"""
Assistant Mode: {option}

Student Request:
{user_input}

Provide:

1. Explanation
2. Recommended Solution
3. Best Practices
4. Common Mistakes
5. Learning Tips
"""

            answer = ask_agent(prompt)

        st.success("Analysis Complete")

        st.markdown("## 🤖 CoachDevOps AI Response")

        st.markdown(answer)

    else:
        st.warning(
            "Please enter a question, requirement, code snippet, YAML file, log output, or error message."
        )

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown("---")

st.caption(
    "🚀 CoachDevOps AI Lab | Learn DevOps, Cloud, Kubernetes, DevSecOps & SRE with AI"
)
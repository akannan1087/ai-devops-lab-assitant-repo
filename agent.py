import os
from openai import OpenAI
from dotenv import load_dotenv

from prompts import (
    DEFAULT_PROMPT,
    JENKINS_PROMPT,
    GITLAB_PROMPT,
    GITHUB_ACTIONS_PROMPT,
    KUBERNETES_PROMPT,
    TERRAFORM_PROMPT,
    DEVSECOPS_PROMPT,
    SRE_PROMPT,
    INTERVIEW_PROMPT,
)

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_system_prompt(mode):
    if mode == "Jenkins Expert":
        return JENKINS_PROMPT

    elif mode == "GitLab CI/CD Expert":
        return GITLAB_PROMPT

    elif mode == "GitHub Actions Expert":
        return GITHUB_ACTIONS_PROMPT

    elif mode == "Kubernetes Expert":
        return KUBERNETES_PROMPT

    elif mode == "Terraform Expert":
        return TERRAFORM_PROMPT

    elif mode == "DevSecOps Expert":
        return DEVSECOPS_PROMPT

    elif mode == "SRE Incident Analysis":
        return SRE_PROMPT

    elif mode == "DevOps Interview Coach":
        return INTERVIEW_PROMPT

    else:
        return DEFAULT_PROMPT


def ask_agent(mode, user_question):
    system_prompt = get_system_prompt(mode)

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_question
            }
        ]
    )

    return response.output_text

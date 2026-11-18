# CoachDevOps AI Lab Assistant

Build your first AI-powered DevOps assistant with Python, Streamlit, and the OpenAI API. Choose a learning mode, enter a question or a sanitized code or log snippet, and get an explanation with a recommended solution.

## Prerequisites

- Git and Python 3.11 or newer
- An OpenAI API key from a project with API billing or credits and access to `gpt-4.1-mini`
- Internet access to install dependencies and call the OpenAI API

## Run locally on macOS or Linux

### 1. Clone the repo and install dependencies

```bash
git clone https://github.com/akannan1087/ai-devops-lab-assitant-repo.git
cd ai-devops-lab-assitant-repo
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

### 2. Configure your API key

Create a file named `.env` in the repository root, next to `app.py`. Replace the placeholder with your own key.

```dotenv
OPENAI_API_KEY=your_openai_api_key_here
```

Keep `.env` and `.venv/` out of Git. Remove credentials and other sensitive information from any input you submit to the app. The app sends your input to the OpenAI API.

### 3. Start the app

```bash
python -m streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501). Press `Ctrl+C` in the terminal to stop the app.

## Try a Jenkins example

1. Select **Jenkins Expert** from the learning mode menu.
2. Enter **“Maven works in my terminal, but my Jenkins pipeline reports `mvn: command not found`. What should I check on the build agent?”**
3. Click **Ask CoachDevOps AI**. Use the response to identify a likely cause and a way to verify it.

Other learning modes cover GitLab CI/CD, GitHub Actions, Kubernetes, Terraform, DevSecOps, SRE incident analysis, and DevOps interview prep. **General DevOps Assistant** and **Generate CI/CD Pipeline** use the default system prompt.

## How it works

| File | Responsibility |
| --- | --- |
| [app.py](app.py) | Collects the learning mode and question, requests a structured answer, and displays the response. |
| [agent.py](agent.py) | Selects the system prompt and calls the OpenAI Responses API with `gpt-4.1-mini`. |
| [prompts.py](prompts.py) | Defines the instructions for each specialist mode and the default assistant. |
| [requirements.txt](requirements.txt) | Lists Streamlit, the OpenAI SDK, and python-dotenv. |

Each submission triggers one model call. The app displays guidance and code examples for the student to review. Students run any suggested commands themselves.

## Lab exercise

Add an **Azure DevOps Expert** learning mode. Write its system prompt in `prompts.py`, map the new mode to that prompt in `agent.py`, and add the mode to the menu in `app.py`. Ask both the new mode and **General DevOps Assistant** the same question about Maven on an Azure Pipelines self-hosted agent. Compare how the prompts shape the answers.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| Python cannot import Streamlit or OpenAI | Activate `.venv` and rerun `python -m pip install -r requirements.txt`. |
| The API key is missing or rejected | Check that `.env` is next to `app.py`, the variable is named `OPENAI_API_KEY`, and the key is valid. Restart Streamlit after editing the file. |
| The API reports insufficient quota | Check the billing, credits, and usage limits for the OpenAI API project associated with your key. |

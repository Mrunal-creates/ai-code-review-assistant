# AI Code Review Assistant

AI Code Review Assistant is a web application that automatically analyzes source code and GitHub repositories to identify bugs, security vulnerabilities, performance issues, and code quality concerns.

The project combines static analysis tools with Large Language Models to generate actionable code review feedback in a structured and developer-friendly format.

## Features

* AI-powered code reviews using Gemini
* GitHub repository analysis
* Pylint integration for code quality checks
* Bandit integration for security scanning
* Performance and optimization suggestions
* Production-ready code recommendations
* REST API built with FastAPI
* Interactive web interface
* Swagger API documentation

## Tech Stack

**Backend**

* Python
* FastAPI
* LangChain

**AI**

* Google Gemini API

**Static Analysis**

* Pylint
* Bandit

**Repository Analysis**

* GitPython

**Frontend**

* HTML
* CSS
* JavaScript

## Project Structure

```text
app/
├── main.py
├── reviewer.py
├── github_review.py
├── repository_reviewer.py
├── prompts.py
└── models.py

static/
templates/

requirements.txt
README.md
```

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/Mrunal-creates/ai-code-review-assistant.git
cd ai-code-review-assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key
```

### Run the Application

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

## Example Capabilities

* Detect hardcoded credentials
* Identify SQL injection risks
* Review repository-level code quality
* Suggest performance improvements
* Recommend secure coding practices
* Generate optimized code versions

## Future Improvements

* User authentication
* Review history tracking
* PDF report export
* CI/CD integration
* Multi-LLM support

## Author

Mrunal Parashar


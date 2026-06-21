# 🚀 AI Code Review Assistant

An AI-powered code review platform that performs intelligent source code analysis, static security scanning, repository-level reviews, and automated optimization recommendations using Gemini AI, FastAPI, Pylint, and Bandit.

---

## 📌 Overview

AI Code Review Assistant helps developers improve code quality by automatically identifying:

- Bugs & Logical Issues
- Security Vulnerabilities
- Performance Bottlenecks
- Code Quality Issues
- Maintainability Problems
- Industry Best Practice Violations

The platform supports both:

1. Individual Code Snippet Reviews
2. Full GitHub Repository Reviews

---

## ✨ Features

### 🤖 AI-Powered Code Review

- Gemini AI-based code analysis
- Context-aware recommendations
- Detailed review reports
- Production-readiness assessment

### 🐞 Bug Detection

- Syntax issues
- Logical flaws
- Runtime risks
- Edge case identification

### 🛡 Security Analysis

- Hardcoded credentials detection
- SQL Injection detection
- Insecure coding practices
- Security severity classification

### ⚡ Performance Optimization

- Complexity analysis
- Inefficient loop detection
- Optimization recommendations
- Scalability insights

### ✨ Code Quality Assessment

- Readability review
- Maintainability analysis
- Naming convention suggestions
- Refactoring recommendations

### 📂 GitHub Repository Review

- Clone public repositories
- Analyze source code files
- Generate repository-wide review reports
- Architecture observations

### 🔍 Static Code Analysis

#### Pylint Integration

- Code quality scoring
- Linting recommendations
- Coding standard enforcement

#### Bandit Integration

- Security vulnerability scanning
- Risk identification
- Secure coding recommendations

### 🌐 Modern Web Interface

- FastAPI Backend
- HTML/CSS/JavaScript Frontend
- Interactive Review Dashboard
- Swagger API Documentation

---

## 🏗 Tech Stack

### Backend

- Python
- FastAPI
- LangChain

### AI

- Google Gemini API

### Static Analysis

- Pylint
- Bandit

### Repository Analysis

- GitPython

### Frontend

- HTML5
- CSS3
- JavaScript

### Development Tools

- Git
- GitHub
- Virtual Environment

---

## 📁 Project Structure

```text
ai-code-review-assistant/

├── app/
│   ├── main.py
│   ├── reviewer.py
│   ├── github_review.py
│   ├── repository_reviewer.py
│   ├── prompts.py
│   └── models.py
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/Mrunal-creates/ai-code-review-assistant.git

cd ai-code-review-assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure Gemini API

Create:

```text
.env
```

Add:

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

## ▶ Run Application

```bash
uvicorn app.main:app --reload
```

Application:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

## 📋 API Endpoints

### Review Source Code

```http
POST /review
```

Example:

```json
{
  "language": "python",
  "code": "print('Hello World')"
}
```

---

### Review GitHub Repository

```http
POST /review-repo
```

Example:

```json
{
  "repo_url": "https://github.com/user/repository"
}
```

---

## 📈 Future Enhancements

- Repository-wide File-by-File Reviews
- Review History Database
- User Authentication
- PDF Report Export
- Monaco Code Editor
- GitHub OAuth
- CI/CD Integration
- Multi-LLM Support

---

## 🎯 Resume Highlights

- Developed an AI-powered code review platform using FastAPI, LangChain, and Gemini AI.
- Integrated Pylint and Bandit for static code analysis and security scanning.
- Built GitHub repository analysis functionality using GitPython.
- Designed RESTful APIs and an interactive frontend for real-time code reviews.
- Automated bug detection, vulnerability analysis, performance optimization, and code quality assessment.

---

## 📜 License

MIT License

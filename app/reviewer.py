import os

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from app.prompts import REVIEW_PROMPT

from app.analyzers.pylint_analyzer import run_pylint
from app.analyzers.bandit_analyzer import run_bandit


load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


def review_code(language: str, code: str):

    try:

        pylint_report = run_pylint(code)

    except Exception as e:

        pylint_report = f"Pylint failed: {str(e)}"

    try:

        bandit_report = run_bandit(code)

    except Exception as e:

        bandit_report = f"Bandit failed: {str(e)}"

    prompt = REVIEW_PROMPT.format(
        language=language,
        code=code,
        pylint_report=pylint_report,
        bandit_report=bandit_report
    )

    try:

        response = llm.invoke(prompt)

        return response.content

    except Exception as e:

        return f"AI Review Failed: {str(e)}"
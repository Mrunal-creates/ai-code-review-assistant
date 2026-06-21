from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from app.models import CodeReviewRequest
from app.reviewer import review_code

from app.models import RepoReviewRequest

from app.repository_reviewer import (
    review_repository
)

app = FastAPI(title="AI Code Review Assistant")

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

templates = Jinja2Templates(
    directory="templates"
)


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/review")
def review(request: CodeReviewRequest):

    result = review_code(
        request.language,
        request.code
    )

    return {
        "review": result
    }

@app.post("/review-repo")
def review_repo(
    request: RepoReviewRequest
):

    result = review_repository(
        request.repo_url
    )

    return {
        "review": result
    }

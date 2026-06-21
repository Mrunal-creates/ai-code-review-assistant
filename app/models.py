from pydantic import BaseModel


class CodeReviewRequest(BaseModel):
    language: str
    code: str

class RepoReviewRequest(BaseModel):
    repo_url: str

    
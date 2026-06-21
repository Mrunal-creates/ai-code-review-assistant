from app.github_review import (
    clone_repository,
    get_code_files,
    read_repository_code
)

from app.reviewer import review_code


def review_repository(repo_url):

    repo_path = clone_repository(
        repo_url
    )

    files = get_code_files(
        repo_path
    )

    code = read_repository_code(
        files
    )

    return review_code(
        "Repository",
        code
    )
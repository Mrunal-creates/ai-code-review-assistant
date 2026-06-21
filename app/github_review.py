from git import Repo
import tempfile
import os


def clone_repository(repo_url):

    temp_dir = tempfile.mkdtemp()

    Repo.clone_from(
        repo_url,
        temp_dir
    )

    return temp_dir


def get_code_files(path):

    files = []

    for root, _, filenames in os.walk(path):

        for file in filenames:

            if file.endswith(
                (
                    ".py",
                    ".java",
                    ".js",
                    ".cpp",
                    ".c",
                    ".cs",
                    ".ts"
                )
            ):

                files.append(
                    os.path.join(root, file)
                )

    return files

def read_repository_code(files):

    repository_code = ""

    for file in files:

        try:

            with open(
                file,
                "r",
                encoding="utf-8",
                errors="ignore"
            ) as f:

                repository_code += f"\n\nFILE: {file}\n"

                repository_code += f.read()

        except Exception:

            pass

    return repository_code
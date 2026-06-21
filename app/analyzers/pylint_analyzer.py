import tempfile
import subprocess
import os


def run_pylint(code: str):

    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".py",
        delete=False,
        encoding="utf-8"
    ) as temp:

        temp.write(code)

        temp_path = temp.name

    try:

        result = subprocess.run(
            ["pylint", temp_path],
            capture_output=True,
            text=True
        )

        return result.stdout

    except Exception as e:

        return f"Pylint Error: {str(e)}"

    finally:

        if os.path.exists(temp_path):
            os.remove(temp_path)
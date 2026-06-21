import tempfile
import subprocess
import os


def run_bandit(code: str):

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
            ["bandit", temp_path],
            capture_output=True,
            text=True
        )

        return result.stdout

    except Exception as e:

        return f"Bandit Error: {str(e)}"

    finally:

        if os.path.exists(temp_path):
            os.remove(temp_path)
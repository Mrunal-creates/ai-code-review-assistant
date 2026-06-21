async function reviewCode() {

    const code =
        document.getElementById("code").value;

    const language =
        document.getElementById("language").value;

    const result =
        document.getElementById("result");

    const loading =
        document.getElementById("loading");

    loading.style.display = "block";

    result.innerText = "";

    try {

        const response =
            await fetch(
                "/review",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        language: language,
                        code: code
                    })
                }
            );

        const data =
            await response.json();

        result.innerText =
            data.review;

    } catch (error) {

        result.innerText =
            "Error: " + error;

    } finally {

        loading.style.display =
            "none";
    }
}


async function reviewRepository() {

    const repoUrl =
        document.getElementById(
            "repo_url"
        ).value;

    const result =
        document.getElementById(
            "result"
        );

    const loading =
        document.getElementById(
            "loading"
        );

    loading.style.display =
        "block";

    result.innerText = "";

    try {

        const response =
            await fetch(
                "/review-repo",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        repo_url: repoUrl
                    })
                }
            );

        const data =
            await response.json();

        result.innerText =
            data.review;

    } catch (error) {

        result.innerText =
            "Error: " + error;

    } finally {

        loading.style.display =
            "none";
    }
}

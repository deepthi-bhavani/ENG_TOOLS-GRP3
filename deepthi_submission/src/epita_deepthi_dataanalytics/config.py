
import os

from dotenv import load_dotenv

load_dotenv()


def get_github_token() -> str:
    token = os.getenv("GITHUB_TOKEN")

    if not token:
        raise ValueError(
            "GITHUB_TOKEN is missing. Add it to your local .env file."
        )

    if not token.startswith(("github_pat_", "ghp_")):
        raise ValueError(
            "GITHUB_TOKEN does not look like a GitHub personal access token."
        )

    return token

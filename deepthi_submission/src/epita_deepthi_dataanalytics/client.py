
import requests

from epita_deepthi_dataanalytics.config import get_github_token


def fetch_live_data() -> dict:
    token = get_github_token()

    response = requests.get(
        "https://api.github.com/user",
        headers={"Authorization": f"Bearer {token}"},
        timeout=15,
    )
    response.raise_for_status()

    user = response.json()

    return {
        "status": "OK",
        "github_login": user.get("login", "Unknown"),
        "public_profile": user.get("html_url", "Unknown"),
        "public_repositories": user.get("public_repos", 0),
        "followers": user.get("followers", 0),
    }

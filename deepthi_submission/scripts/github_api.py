
import os
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("GITHUB_TOKEN")

if not token:
    raise ValueError("GITHUB_TOKEN is missing. Check your .env file.")

response = requests.get(
    "https://api.github.com/user",
    headers={"Authorization": f"Bearer {token}"},
    timeout=15,
)

print("Status code:", response.status_code)

if response.status_code == 200:
    user = response.json()
    print("GitHub login:", user.get("login"))
    print("Public profile:", user.get("html_url"))
else:
    print("API error:", response.text)

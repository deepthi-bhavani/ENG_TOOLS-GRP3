
# TP2 Report — Python Environment

## 1. Python Environment Inspection

I created `scripts/inspect_env.py` to display the Python version, executable path, operating system, current working directory, and virtual environment information.

## 2. Global Python vs. uv

- Global Python uses the Python interpreter installed on the computer by default.
- `uv run` runs commands using the project's managed environment and dependencies.
- A project environment helps keep dependencies separate between projects.

## 3. Git Ignore

The `.gitignore` file excludes the virtual environment, Python cache files, `.env` secrets, and build artifacts from Git.

## 4. API Authentication and Secret Management

I stored my GitHub personal access token in a `.env` file and used `python-dotenv` to load it into my Python script. The script sends a request to the GitHub REST API using the token in the Authorization header. The API returned status code 200, confirming that authentication was successful. I added `.env` to `.gitignore` to prevent accidentally uploading the token to GitHub.

## 5. Dependency Management and Lock File

I used `uv add` to install the required packages: requests, python-dotenv, and rich. I added pytest as a development dependency using `uv add --dev pytest`.

I ran `uv tree` to view the project's dependencies and `uv lock` to check and update the lock file. The `uv.lock` file records the resolved package versions and package information, helping maintain consistent environments.

## 6. Semantic Versioning

Semantic Versioning uses three numbers in the format MAJOR.MINOR.PATCH.

- MAJOR: Changes that are not backward-compatible.
- MINOR: New features that remain backward-compatible.
- PATCH: Backward-compatible bug fixes.

For example, version 2.3.1 means MAJOR = 2, MINOR = 3, and PATCH = 1.

## 7. Debugging Challenge

### Problem Identified

The API record parser returned `volume` and `weight` as strings because the `split(",")` method produces string values. When the program attempted to multiply these two strings, it raised a `TypeError`.

### Fix Applied

I used the VS Code debugger to inspect the execution and identify the type mismatch. I converted the values to integers in `parse_api_record()`:

```python
"volume": int(parts[2]),
"weight": int(parts[4]),
```

### Verified Result

- Successful entries: 3
- Total volume: 650
- Average volume: approximately 216.67
- High-impact entries: 1

The corrected program now calculates the weighted metric and aggregates the successful records correctly.


## 8. Environment Configuration and Secret Management

I created `.env.template` to show which environment variable is required without including any real credentials. My local `.env` file stores the actual GitHub token and is excluded from Git through `.gitignore`.

I created `config.py` with a `get_github_token()` function. It checks whether the token exists and whether it resembles a GitHub personal access token. The API client uses this function to retrieve the token before sending the authenticated request.

This separates configuration from API logic and helps prevent accidental exposure of credentials.

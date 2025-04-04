import pulumi
from repo import repo
import file  # Import file.py to run the file creation logic

# Export the repository name and URL
pulumi.export("repo_name", repo.name)
pulumi.export("repo_url", repo.html_url)

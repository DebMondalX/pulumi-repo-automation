import pulumi
from repo import repo

# Export the repository name and URL
pulumi.export("repo_name", repo.name)
pulumi.export("repo_url", repo.html_url)

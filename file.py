import pulumi
import pulumi_github as github
from repo import exported_repo
import time

# Wait for a brief time to ensure repository is initialized before creating files.
time.sleep(10)  

# Create the file within the existing repository
repository_file = github.RepositoryFile("file-in-repo",
    repository=exported_repo.name,  # Use the repo created in repo.py
    file="sample-file.txt",
    branch="main",  
    content="Hello, Pulumi!",
    commit_message="Adding an example file",
    overwrite_on_create=True
)

pulumi.export("repository_url", exported_repo.html_url)

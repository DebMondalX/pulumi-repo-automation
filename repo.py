import pulumi
import pulumi_github as github

# Create the repository with an auto-generated README to ensure the main branch exists
repo = github.Repository("my-repo",
    name="my-repo",
    auto_init=True,  # auto-init creates a repo with a default branch and README
    description="My Pulumi-created repo")

# Export the repository name and URL
pulumi.export("repo_name", repo.name)
pulumi.export("repo_url", repo.html_url)

# Expose the repository object for use in file.py
exported_repo = repo

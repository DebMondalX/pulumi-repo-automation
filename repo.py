import pulumi
import pulumi_github as github

# Get config values from user input
config = pulumi.Config()
repo_name = config.require("repoName")  # requires user to set this
repo_description = config.get("repoDescription") or "My Pulumi-created repo"  # optional, with default
is_private = config.get_bool("repoPrivate") or False

# Create the repository with an auto-generated README to ensure the main branch exists
repo = github.Repository(repo_name,
    name= repo_name,
    auto_init=True,  # auto-init creates a repo with a default branch and README
    description=repo_description,
    visibility="private" if is_private else "public"
    )

# Export the repository name and URL
pulumi.export("repo_name", repo.name)
pulumi.export("repo_url", repo.html_url)

# Expose the repository object for use in file.py
exported_repo = repo

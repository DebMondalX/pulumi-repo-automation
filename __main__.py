import pulumi
import pulumi_github as github

# Define the GitHub repository
repo = github.Repository("my-repo",
    name="my-repo",
    description="A Pulumi-managed GitHub repository",
    visibility="public"
)

# Define branch protection (without required PR reviews)
branch_protection = github.BranchProtection("my-repo-protection",
    repository_id=repo.name,
    pattern="main"
)

# Export the repository name
pulumi.export("repo_name", repo.name)

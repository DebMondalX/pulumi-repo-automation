import pulumi
import pulumi_github as github

# Read config values from Pulumi Automation API
config = pulumi.Config()
repo_name = config.require("repoName")
repo_description = config.require("repoDescription")
is_private = config.get_bool("repoPrivate") or False

# Create the repository
repo = github.Repository(repo_name,
    name=repo_name,
    auto_init=True,
    description=repo_description,
    visibility="private" if is_private else "public"
)

# Export repo metadata
pulumi.export("repo_name", repo.name)
pulumi.export("repo_url", repo.html_url)

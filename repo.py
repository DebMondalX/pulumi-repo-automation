import pulumi
import pulumi_github as github

# Get config values from user input
config = pulumi.Config()
repo_name = config.require("repoName")  
repo_description = config.get("repoDescription") or "My Pulumi-created repo"  
is_private = config.get_bool("repoPrivate") or False


repo = github.Repository(repo_name,
    name= repo_name,
    auto_init=True,  
    description=repo_description,
    visibility="private" if is_private else "public"
    )


pulumi.export("repo_name", repo.name)
pulumi.export("repo_url", repo.html_url)


exported_repo = repo

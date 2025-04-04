import pulumi.automation as auto
import os

def pulumi_program():
    import repo  # This triggers your Pulumi resources to be created from repo.py
    import file  # This will create the README or other files

def run():
    repo_name = input("📦 Enter repository name: ")
    repo_description = input("📝 Enter description (optional): ") or "My Pulumi-created repo"
    visibility = input("🔐 Should the repo be private? (yes/no): ").strip().lower()
    is_private = visibility == "yes"

    # Create or select stack
    stack = auto.create_or_select_stack(
        stack_name="dev",
        project_name="github-repo",
        program=pulumi_program  # Here's the fix!
    )

    print("🔧 Setting config...")
    stack.set_config("repoName", auto.ConfigValue(value=repo_name))
    stack.set_config("repoDescription", auto.ConfigValue(value=repo_description))
    stack.set_config("repoPrivate", auto.ConfigValue(value=str(is_private).lower()))

    print("🔄 Installing dependencies...")
    os.system("pip install -r requirements.txt")  # Make sure dependencies are installed

    print("🚀 Running Pulumi up...")
    up_res = stack.up(on_output=print)

    print("\n✅ Repo Created!")
    print(f"📦 Repo Name: {up_res.outputs['repo_name'].value}")
    print(f"🌍 Repo URL: {up_res.outputs['repo_url'].value}")

if __name__ == "__main__":
    run()

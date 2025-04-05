# Automating GitHub Repository Setup with Pulumi

This project uses the **Pulumi Automation API** and **Pulumi GitHub Provider** to automate the creation and configuration of GitHub repositories — including initialization, file creation, and custom settings — all from a Python script.

## Table of Contents

- [Features](#-features)
- [Installation](#️-installation)
- [How to Run](#-how-to-run)
- [Use Cases](#-use-cases)
- [Project Structure](#-project-structure)
- [References](#-references)

---

## Features

- Creates GitHub repositories (public or private).
- Automatically initializes with a README or custom files.
- Uses **Pulumi Automation API** to manage stack programmatically.
- Allows user input for customization.
- Clean CLI interaction for automation scripts.

---

## Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/pulumi-repo-automation.git
   cd pulumi-repo-automation
2. **Set up Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt   
4. **Export your GitHub token**  
   You can either set this in a .env file or export it directly:
   ```bash
   export GITHUB_TOKEN=your_token_here  # For Unix/macOS
   set GITHUB_TOKEN=your_token_here     # For Windows
----
## How to Run
Run the script:
   ```bash
    python run.py  
   ```
#### You’ll be prompted to enter:  
- Repository name  
- Description (optional)  
- Visibility (public/private)  

#### Pulumi will then:

Spin up the stack

Set config values dynamically

Create the repo

Add an example file

Output the repo URL  

---
## 💡 Use Cases
Quickly bootstrap repos for projects or teams.

Automate GitHub org workflows.

Integrate with CI/CD to generate project infra.

---
## References
[Pulumi Automation API Docs](https://www.pulumi.com/docs/iac/using-pulumi/automation-api/) 

[Pulumi GitHub Provider Docs](https://www.pulumi.com/registry/packages/github/)


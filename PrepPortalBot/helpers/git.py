from github import Github
import os

class Github_Helper():
    def __init__(self, token, repo_owner, repo_name) -> None:
        self.git = Github(token)
        self.repo_owner = repo_owner
        self.repo_name = repo_name
    
    def update_file(self, file_path, branch, commit_msg):
        repo = self.git.get_repo(f"{self.repo_owner}/{self.repo_name}")
        content = repo.get_contents(os.path.basename(file_path))
        with open(file_path, "r") as file:
            file_content = file.read()
        repo.update_file(content.path, commit_msg, file_content, content.sha, branch=branch)
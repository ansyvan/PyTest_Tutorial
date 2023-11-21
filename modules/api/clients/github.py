import requests


class GitHub:

    def get_user(self, username):
        r = requests.get(
            f"https://api.github.com/users/{username}"
            )
        body = r.json()

        return body
    
    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories", 
            params={"q": name}
            )
        body = r.json()

        return body
    

# This part is an individual task to practice testing skills for the QA Auto Course
    
    github_headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer randomsymbols",     # input a valid token here
        "X-GitHub-Api-Version": "2022-11-28",
        }
    
    def get_info_user(self, username, github_headers):
        r = requests.get(
            f"https://api.github.com/users/{username}/hovercard",
            headers=github_headers
            )
        body = r.json()

        return body
    
    
    def get_info_user_repository(self, username, repository, repo_id, github_headers):
        r = requests.get(
            f"https://api.github.com/users/{username}/hovercard",
            params={"subject_type": repository, "subject_id": repo_id},
            headers=github_headers
            )
        body = r.json()

        return body
    

    def list_users(self, users_per_page=30):
        r = requests.get(
            f"https://api.github.com/users",
            params={"per_page": users_per_page}
            )
        body = r.json()

        return body


    def list_emojis(self):
        r = requests.get(
            "https://api.github.com/emojis"
            )
        body = r.json()

        return body
    

    def list_branches(self, owner, repo):
        r = requests.get(
            f"https://api.github.com/repos/{owner}/{repo}/branches"
            )
        body = r.json()

        return body
import requests


class GitHub:

    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
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

    
    def get_info_user(self, username, headers):
        r = requests.get(
            f"https://api.github.com/users/{username}/hovercard",
            headers
            )
        body = r.json()

        return body
    
    
    def get_info_user_repository(self, username, repository, repo_id):
        r = requests.get(
            f"https://api.github.com/users/{username}/hovercard",
            params={"subject_type": repository, "subject_id": repo_id}
            )
        body = r.json()

        return body
    

    def list_users(self):
        r = requests.get(f"https://api.github.com/users",
        params={"per_page": 30}
        )
        body = r.json()

        return body


    def list_emojis(self):
        r = requests.get(
            "https://api.github.com/emojis"
        )
        body = r.json()

        return body
    

    def list_branches(self, owner, repo, commit_sha):
        r = requests.get(
            f"https://api.github.com/repos/{owner}/{repo}/commits/{commit_sha}/branches-where-head"
        )
        body = r.json()

        return body
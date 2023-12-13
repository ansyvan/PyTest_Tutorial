import pytest
from modules.api.clients.github import GitHub


class User:

    def __init__(self):
        self.name = None
        self.second_name = None

    def create(self):
        self.name = 'Andriana'
        self.second_name = 'Syvanych'

    def remove(self):
        self.name = ''
        self.second_name = ''


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()


@pytest.fixture
def github_api():
    api = GitHub()
    yield api

# This part is an individual task to practice testing skills after the QA Automation Course.

@pytest.fixture
def github_headers():
    return {
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer myValidToken",  # input a valid token here
        "X-GitHub-Api-Version": "2022-11-28",
    }
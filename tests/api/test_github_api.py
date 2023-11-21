import pytest

# This part is an individual task to practice testing skills for the QA Auto Course.

# Tests that require a user authentication token.
# To pass this test input a valid token in the conftest.py file.
@pytest.mark.api
def test_info_about_user_with_valid_token(github_api, github_headers):
    r = github_api.get_info_user('ansyvan', github_headers)
    assert 'Owns this repository' in r
    print(r)

@pytest.mark.api
def test_info_about_user_with_invalid_token(github_api, github_headers):
    r = github_api.get_info_user('ansyvan', github_headers)
    assert r['message'] == 'Bad credentials'
    print(r)

# Testing list of users.
@pytest.mark.api
def test_number_of_users_on_page(github_api):
    users_per_page = 30
    r = github_api.list_users(users_per_page)
    assert len(r) == users_per_page

@pytest.mark.api
def test_user_is_first_in_list(github_api):
    r = github_api.list_users()
    assert 'mojombo' in r[0]['login']

# Emoji tests.
@pytest.mark.api
def test_emoji_amount(github_api):
    r = github_api.list_emojis()
    assert len(r) == 1877

@pytest.mark.api
def test_emoji_exists(github_api):
    emoji = github_api.list_emojis()
    assert 'alarm_clock' in emoji

@pytest.mark.api
def test_emoji_not_exists(github_api):
    emoji = github_api.list_emojis()
    assert 'not_emoji' not in emoji

# Testing the list of branches in the repository.
@pytest.mark.api
def test_commit(github_api):
    r = github_api.list_branches('ansyvan', 'pytest_tutorial')
    assert len(r) >= 2      # The number of branches is 2 or more in case more branches will be added.
    assert 'main' in r
    assert 'one_more_branch' in r


# This part is from QA Automation Course.

@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] >= 50   # The number of repositories is 50 or more in case more repos will be added.
    assert 'become-qa-auto' in r['items'][0]['name']

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0
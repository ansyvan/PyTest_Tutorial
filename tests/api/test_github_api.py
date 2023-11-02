import pytest

# 1
@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

# 2
@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'

# 3
@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 50
    assert 'become-qa-auto' in r['items'][0]['name']

# 4
@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0

# 5
@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0




# This part is an individual task to practice testing skills for the QA Auto Course

#github_api = GitHub(api_token="randomsymbols")

# 6
@pytest.mark.api
def test_info_about_user(github_api):
    headers = {"Authorization": "random symbols"}
    r = github_api.get_info_user('ansyvan', headers)
    #assert r['message'] == 'Requires authentication'
    print(r)

# 7
@pytest.mark.api
def test_info_about_user_repo(github_api):
    r = github_api.get_info_user_repository('ansyvan', 'repository', '699413145')
    assert r['message'] == 'Requires authentication'
    print(r)

# 8
@pytest.mark.api
def test_number_of_users_on_page(github_api):
    r = github_api.list_users()
    assert len(r) == 30

# 9
@pytest.mark.api
def test_user_is_first_in_list(github_api):
    r = github_api.list_users()
    assert 'mojombo' in r[0]['login']

# 10
@pytest.mark.api
def test_emoji_amount(github_api):
    r = github_api.list_emojis()
    assert len(r) == 1877

# 11
@pytest.mark.api
def test_emoji_exists(github_api):
    emoji = github_api.list_emojis()
    assert 'alarm_clock' in emoji

# 12
@pytest.mark.api
def test_emoji_not_exists(github_api):
    emoji = github_api.list_emojis()
    assert 'not_emoji' not in emoji

# 13
@pytest.mark.api
def test_commit(github_api):
    owner = 'ansyvan'
    repo = 'pytest_tutorial'
    commit_sha = '65357753e9b91ce5f243fcc8bb416c6d677ded49'
    r = github_api.list_branches(owner, repo, commit_sha)
    #assert r['message'] == '65357753e9b91ce5f243fcc8bb416c6d677ded49'
    #assert r['message'] == commit_sha
    #assert '65357753e9b91ce5f243fcc8bb416c6d677ded49' in r
    print(r)
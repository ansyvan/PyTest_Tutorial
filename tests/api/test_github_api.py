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


# 6
@pytest.mark.api
def test_info_about_user(github_api):

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer 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",     # input token here
        "X-GitHub-Api-Version": "2022-11-28",}
    r = github_api.get_info_user('ansyvan', headers)
    assert 'Owns this repository' in r
    # if you don't have a token use the line below instead of assert 'Owns this repository' in r
    # assert r['message'] == 'Requires authentication'
    print(r)

# 7
@pytest.mark.api
def test_info_about_user_repo(github_api):
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer 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",     # input token here
        "X-GitHub-Api-Version": "2022-11-28",}
    r = github_api.get_info_user_repository('ansyvan', 'repository', '699413145', headers)
    assert any(context['message'] == 'Owns this repository' for context in r.get('contexts', []))
    # if you don't have a token use the line below instead of assert any(context['message'] == 'Owns this repository' for context in r.get('contexts', []))
    # assert r['message'] == 'Requires authentication'

# 8
@pytest.mark.api
def test_number_of_users_on_page(github_api):
    users_per_page = 30
    r = github_api.list_users(users_per_page)
    assert len(r) == users_per_page

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
    r = github_api.list_branches('ansyvan', 'pytest_tutorial')

    print(r)
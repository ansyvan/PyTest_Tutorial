import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_username():
    # create an Object for browser control
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
        )

    # open page https://github.com/login
    driver.get("https://github.com/login")

    # find the field where an incorrect name will be inserted
    login_elem = driver.find_element(By.ID, "login_field")

    # enter an incorrect name or email address
    login_elem.send_keys("sergiibutenko@mistakeinemail.com")

    # find the field where an incorrect will be inserted
    pass_elem = driver.find_element(By.ID, "password")

    # insert an incorrect password
    pass_elem.send_keys("wrong password")

    # find Sign In button
    btn_elem = driver.find_element(By.NAME, "commit")

    # simulate a left mouse button click
    btn_elem.click()

    # check that the page title is what we expect
    assert driver.title == "Sign in to GitHub · GitHub"

    # закриваємо браузер
    driver.close()
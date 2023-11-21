import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_username():
    # Create an Object for browser control.
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
        )

    # Open page https://github.com/login
    driver.get("https://github.com/login")

    # Find the field where an incorrect name will be inserted.
    login_elem = driver.find_element(By.ID, "login_field")

    # Enter an incorrect name or email address.
    login_elem.send_keys("sergiibutenko@mistakeinemail.com")

    # Find the field where an incorrect will be inserted.
    pass_elem = driver.find_element(By.ID, "password")

    # Insert an incorrect password.
    pass_elem.send_keys("wrong password")

    # Find Sign In button.
    btn_elem = driver.find_element(By.NAME, "commit")

    # Simulate a left mouse button click.
    btn_elem.click()

    # Check that the page title is what we expect.
    assert driver.title == "Sign in to GitHub · GitHub"

    # Close the browser.
    driver.close()
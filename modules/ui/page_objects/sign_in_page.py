from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = 'http://github.com/login'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        # find the field where an incorrect name or email will be inserted
        login_elem = self.driver.find_element(By.ID, "login_field")

        # input an incorrect user's name or email
        login_elem.send_keys(username)

        # find the field where an incorrect password will be inserted
        pass_elem = self.driver.find_element(By.ID, "password")

        # input the incorrect password
        pass_elem.send_keys(password)

        # find 'sign in' button
        btn_elem = self.driver.find_element(By.NAME, "commit")

        # simulate a left mouse button click
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title
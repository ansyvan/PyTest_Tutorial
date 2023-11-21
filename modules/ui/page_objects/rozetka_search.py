# This part is an individual task to practice testing skills after the QA Automation Course

from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RozetkaSearch(BasePage):
    URL = 'https://rozetka.com.ua/ua'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(RozetkaSearch.URL)

    def search_product(self, search_keywords):

        wait = WebDriverWait(self.driver, 10)
        
        search_elem = wait.until(EC.presence_of_element_located((By.NAME, "search")))
        search_elem.send_keys(search_keywords)
        search_elem.submit()

    def check_title(self, expected_title):
        wait = WebDriverWait(self.driver, 20)
        return wait.until(EC.title_is(expected_title))
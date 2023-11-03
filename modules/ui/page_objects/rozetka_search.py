from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class RozetkaSearch(BasePage):
    URL = 'https://rozetka.com.ua/ua'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(RozetkaSearch.URL)

    def search_product(self, search_keywords):
        
        search_elem = self.driver.find_element(By.NAME, "search")

        search_elem.send_keys(search_keywords)

        search_elem.submit()
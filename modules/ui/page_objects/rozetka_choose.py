from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class RozetkaChoose(BasePage):
    URL = 'https://rozetka.com.ua/ua/apple/c4627486/#search_text=apple'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(RozetkaChoose.URL)


    def choose_product(self):

        product_elem = self.driver.find_element(By.CSS_SELECTOR, "body > app-root > div > div > rz-super-portal > div > main > section > div:nth-child(3) > rz-dynamic-widgets > rz-widget-list:nth-child(2) > section > ul > li:nth-child(1) > rz-list-tile > div > a.tile-cats__heading.tile-cats__heading_type_center.ng-star-inserted")

        product_elem.click()

        product_elem = self.driver.find_element(By.CSS_SELECTOR, "css=.catalog-grid__cell:nth-child(1) .goods-tile__title")

        product_elem.click()

    #def add_product_to_cart(self):

        #buy_elem = self.driver.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[2]/rz-product-main-info/div[1]/div[1]/div[3]/rz-product-buy-btn/app-buy-button/button/span')

        #buy_elem.click()

        #buy_elem = self.driver.find_element(By.CSS_SELECTOR, ".button_size_large > span")

        #buy_elem.click()

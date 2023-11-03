from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class RozetkaChoose(BasePage):
    URL = 'https://rozetka.com.ua/ua/'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(RozetkaChoose.URL)


    def choose_product(self):

        product_elem = self.driver.find_element(By.XPATH, "/html/body/app-root/div/div/rz-main-page/div/aside/rz-main-page-sidebar/div[1]/rz-sidebar-fat-menu/div/ul/li[2]/a")

        product_elem.click()

        product_elem = self.driver.find_element(By.XPATH, "/html/body/app-root/div/div/rz-main-page/div/main/rz-main-page-content/rz-goods-sections/section[2]/rz-goods-section/ul/li[1]/rz-app-tile/div/div/a[2]")

        product_elem.click()

    #def add_product_to_cart(self):

        #buy_elem = self.driver.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[2]/rz-product-main-info/div[1]/div[1]/div[3]/rz-product-buy-btn/app-buy-button/button/span')

        #buy_elem.click()

        #buy_elem = self.driver.find_element(By.CSS_SELECTOR, ".button_size_large > span")

        #buy_elem.click()

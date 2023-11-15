# This part is an individual task to practice testing skills after the QA Automation Course

from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AmazonChooseProduct(BasePage):
    URL = 'https://www.amazon.com/'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(AmazonChooseProduct.URL)
        # Sometimes the other design of the Home page opens.
        # It have no burger menu with categories, so the test fails
        # I think the Reload method should be added to prevent the failure

    def shop_by_category(self, category, subcategory):

        # Create a WebDriverWait instance
        wait = WebDriverWait(self.driver, 10)

        # Locate the "Shop by Category" element
        category_elem = wait.until(EC.element_to_be_clickable((By.ID, "nav-hamburger-menu")))
        category_elem.click()

        # Hover over the "Shop by Category" element to reveal the dropdown
        ActionChains(self.driver).move_to_element(category_elem).perform()

        # Locate the "Computers" element and click
        category_elem = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, category)))
        self.driver.execute_script("arguments[0].scrollIntoView();", category_elem)
        self.driver.execute_script("arguments[0].click();", category_elem)

        # Locate the "Monitors" element and click
        category_elem = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, subcategory)))
        self.driver.execute_script("arguments[0].scrollIntoView();", category_elem)
        self.driver.execute_script("arguments[0].click();", category_elem)


    def select_product(self):

        product_elem = self.driver.find_element(By.CSS_SELECTOR, "#search > div.s-desktop-width-max.s-desktop-content.s-wide-grid-style-t1.s-opposite-dir.s-wide-grid-style.sg-row > div.sg-col-20-of-24.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div > span.rush-component.s-latency-cf-section > div.s-main-slot.s-result-list.s-search-results.sg-row > div:nth-child(6)")
        product_elem.click()

    def add_to_cart(self):
        # this step can fail if the location is set as Ukraine. 
        # "Add to card" button may be inactive for some regions.
        # While performing this test it worked fine, but in case of failure, keep this in mind
        # create if-else !!!

        buy_btn_elem = self.driver.find_element(By.ID, "add-to-cart-button")
        buy_btn_elem.click()
    
    def check_title(self, expected_title):
        return self.driver.title == expected_title
    
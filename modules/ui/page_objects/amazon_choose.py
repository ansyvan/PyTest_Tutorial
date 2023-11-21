# This part is an individual task to practice testing skills after the QA Automation Course

from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class AmazonChooseProduct(BasePage):
    URL = 'https://www.amazon.com/'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(AmazonChooseProduct.URL)

    # Sometimes the other design of the Home page opens.
    # It have no burger menu with categories, so the test fails.
    # Reload method is to prevent the failure.    
    def reload_page(self):
        self.driver.refresh()

    def shop_by_category(self, category, subcategory):

        # Create a WebDriverWait instance
        wait = WebDriverWait(self.driver, 20)

        # self.reload_page()

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

        wait = WebDriverWait(self.driver, 10)

        # "Add to card" button may be inactive for some regions.
        try:
            buy_btn_elem = wait.until(EC.presence_of_all_elements_located((By.ID, "add-to-cart-button")))
            if buy_btn_elem.is_displayed() and buy_btn_elem.is_enabled():
                buy_btn_elem.click()
                return  # Successfully clicked, no need to check the alternative button
        except TimeoutException:
            pass

        # "Undeliverable buy button" is an inactive button, alternative to "Add to Cart".
        try:
            undeliverable_buy_btn_elem = wait.until(EC.presence_of_element_located((By.ID, "exports_desktop_undeliverable_buybox_cta_feature_div")))
            if undeliverable_buy_btn_elem.is_displayed():
                print("Add to Cart button is not enabled for the current region.")
            else:
                pass
        except TimeoutException:
            print("Neither button is present.")

    # Check if the element with ID "productTitle" is present on the page and has non-empty text.
    def check_text_on_page(self):
       wait = WebDriverWait(self.driver, 10)
       element = wait.until(EC.presence_of_element_located((By.ID, "productTitle")))
       return bool(element.text.strip())
    
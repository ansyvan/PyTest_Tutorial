    # def change_location(self, zipcode):

    #     wait = WebDriverWait(self.driver, 10)

    #     delivery_elem = self.driver.find_element(By.ID, "nav-global-location-slot")
    #     delivery_elem.click()

    #     search_elem = wait.until(EC.element_to_be_clickable((By.ID, "GLUXZipUpdateInput")))
    #     search_elem.send_keys(zipcode)

    #     btn_elem = wait.until(EC.element_to_be_clickable((By.ID, "GLUXZipUpdate")))
    #     btn_elem.click()

    #     btn_elem = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue")))
    #     btn_elem.click()
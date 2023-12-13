# This part is an individual task to practice testing skills for the QA Auto Course.

from modules.ui.page_objects.amazon_choose import AmazonChooseProduct
import pytest


@pytest.mark.ui
@pytest.mark.amazon     # To run tests with multiple markers use: pytest -m "ui and amazon"
def test_choose_product():

    amazon_choose = AmazonChooseProduct()
    amazon_choose.go_to()     # Open Amazon Home page
    amazon_choose.reload_page()
    
    amazon_choose.shop_by_category("Computers", "Monitors")     # Print category and subcategory link text
    amazon_choose.select_product()
    amazon_choose.add_to_cart()
    
    assert amazon_choose.check_text_on_page()
    amazon_choose.close()
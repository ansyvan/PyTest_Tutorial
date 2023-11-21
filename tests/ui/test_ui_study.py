# This part is an individual task to practice testing skills for the QA Auto Course.

from modules.ui.page_objects.rozetka_search import RozetkaSearch
from modules.ui.page_objects.amazon_choose import AmazonChooseProduct
import pytest


@pytest.mark.ui
def test_search_product():

    rozetka_search = RozetkaSearch()     # Create page Object
    rozetka_search.go_to()     # Open page https://rozetka.com.ua/ua/
    rozetka_search.search_product("Apple iPhone 15 128GB Black Titanium")    # Search for the product

    assert rozetka_search.check_title("Інтернет-магазин ROZETKA™: офіційний сайт найпопулярнішого онлайн-гіпермаркету в Україні")
    rozetka_search.close()


@pytest.mark.ui
def test_choose_product():

    amazon_choose = AmazonChooseProduct()
    amazon_choose.go_to()     # Open Amazon Home page
    amazon_choose.reload_page()
    
    amazon_choose.shop_by_category("Computers", "Monitors")     # Print category and subcategory link text
    amazon_choose.select_product()
    amazon_choose.add_to_cart()
    
    assert amazon_choose.check_text_on_page()
    amazon_choose.close()
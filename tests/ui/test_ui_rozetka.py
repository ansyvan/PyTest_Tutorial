# This part is an individual task to practice testing skills for the QA Auto Course.

from modules.ui.page_objects.rozetka_search import RozetkaSearch
import pytest


@pytest.mark.ui
@pytest.mark.rozetka    # To run tests with multiple markers use: pytest -m "ui and rozetka"
def test_search_product():

    rozetka_search = RozetkaSearch()     # Create page Object
    rozetka_search.go_to()     # Open page https://rozetka.com.ua/ua/
    rozetka_search.search_product("Apple iPhone 15 128GB Black Titanium")    # Search for the product

    assert rozetka_search.check_title("Інтернет-магазин ROZETKA™: офіційний сайт найпопулярнішого онлайн-гіпермаркету в Україні")
    rozetka_search.close()
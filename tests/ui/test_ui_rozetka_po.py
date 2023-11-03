from modules.ui.page_objects.rozetka_search import RozetkaSearch
from modules.ui.page_objects.rozetka_choose import RozetkaChoose
import pytest
import time

# This part is an individual task to practice testing skills for the QA Auto Course

@pytest.mark.ui
def test_search_product():

    rozetka_search = RozetkaSearch()     # create page Object

    rozetka_search.go_to()     # open page https://rozetka.com.ua/ua/
    time.sleep(3)

    rozetka_search.search_product("Apple iPhone 15 128GB")    # search for the product
    time.sleep(3)

@pytest.mark.ui
def test_choose_product():

    rozetka_choose = RozetkaChoose()

    rozetka_choose.choose_product()        # choose the product
    time.sleep(3)

   # add_to_cart.add_product_to_cart()
   # time.sleep(3)



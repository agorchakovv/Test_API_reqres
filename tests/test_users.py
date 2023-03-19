import pytest
from search.search_users import SearchHelper 
from base_app import BasePage

@pytest.fixture
def back_browser(browser):
   main_page = BasePage(browser)
   browser.get(main_page.base_url)
   yield browser

def test_list_users(back_browser):
    main_page = BasePage(back_browser)
    main_page = SearchHelper(back_browser)
    main_page.list_users(back_browser)

def test_single_user(browser):
    main_page = BasePage(browser)
    main_page = SearchHelper(browser)
    main_page.single_user(browser)

def test_single_user_not_found(browser):
    main_page = BasePage(browser)
    main_page = SearchHelper(browser)
    main_page.single_user_not_found(browser)
import pytest
from search.search_change_users import SearchHelper 
from base_app import BasePage

@pytest.fixture
def back_browser(browser):
   main_page = BasePage(browser)
   browser.get(main_page.base_url)
   yield browser

def test_create_user(back_browser):
    main_page = BasePage(back_browser)
    main_page = SearchHelper(back_browser)
    main_page.create_user(back_browser)

def test_update_user(browser):
    main_page = BasePage(browser)
    main_page = SearchHelper(browser)
    main_page.update_user(browser)

def test_delete_user(browser):
    main_page = BasePage(browser)
    main_page = SearchHelper(browser)
    main_page.delete_user(browser)
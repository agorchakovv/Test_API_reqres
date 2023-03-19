import pytest
from search.search_main import SearchHelper 
from base_app import BasePage

@pytest.fixture
def back_browser(browser):
   main_page = BasePage(browser)
   browser.get(main_page.base_url)
   yield browser

def test_users(back_browser):
    main_page = BasePage(back_browser)
    main_page = SearchHelper(back_browser)
    main_page.users(back_browser)

def test_not_found(browser):
    main_page = BasePage(browser)
    main_page = SearchHelper(browser)
    main_page.not_found(browser)

def test_create_user(browser):
    main_page = BasePage(browser)
    main_page = SearchHelper(browser)
    main_page.create_user(browser)

def test_delete_user(browser):
    main_page = BasePage(browser)
    main_page = SearchHelper(browser)
    main_page.delete_user(browser)
import pytest
from search.search_authorization import SearchHelper 
from base_app import BasePage

@pytest.fixture
def back_browser(browser):
   main_page = BasePage(browser)
   browser.get(main_page.base_url)
   yield browser

def test_register_pass(back_browser):
    main_page = BasePage(back_browser)
    main_page = SearchHelper(back_browser)
    main_page.register_pass(back_browser)

def test_register_failed(browser):
    main_page = BasePage(browser)
    main_page = SearchHelper(browser)
    main_page.register_fail(browser)

def test_login_pass(browser):
    main_page = BasePage(browser)
    main_page = SearchHelper(browser)
    main_page.login_pass(browser)

def test_login_failed(browser):
    main_page = BasePage(browser)
    main_page = SearchHelper(browser)
    main_page.login_fail(browser)
from selenium.webdriver.common.by import By

class Locators:
    LOCATOR_USERS = (By.CSS_SELECTOR, '[data-id="users"]')
    LOCATOR_NOT_FOUND = (By.CSS_SELECTOR, '[data-id="unknown-single-not-found"]')
    LOCATOR_CREATE_USER = (By.CSS_SELECTOR, '[data-id="post"]')
    LOCATOR_RESPONSE_CODE = (By.CSS_SELECTOR, '.response-code')
    LOCATOR_DELETE_USER = (By.CSS_SELECTOR, '[data-id="delete"]')
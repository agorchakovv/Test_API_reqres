from selenium.webdriver.common.by import By

class LocatorsUsers:
    LOCATOR_LIST_USERS = (By.CSS_SELECTOR, '[data-id="users"]')
    LOCATOR_SINGLE_USER = (By.CSS_SELECTOR, '[data-id="users-single"]')
    LOCATOR_SINGLE_USER_NOT_FOUND = (By.CSS_SELECTOR, '[data-id="users-single-not-found"]')
    LOCATOR_RESPONSE_CODE = (By.CSS_SELECTOR, '.response-code')

class LocatorsResourse:
    LOCATOR_LIST_USERS_RESOURSE = (By.CSS_SELECTOR, '[data-id="unknown"]')
    LOCATOR_SINGLE_USER_RESOURSE = (By.CSS_SELECTOR, '[data-id="unknown-single"]')
    LOCATOR_SINGLE_USER_NOT_FOUND_RESOURSE = (By.CSS_SELECTOR, '[data-id="unknown-single-not-found"]')

class LocatorsChangeUsers:
    LOCATOR_CREATE_USER = (By.CSS_SELECTOR, '[data-id="post"]')
    LOCATOR_UPDATE_USER = (By.CSS_SELECTOR, '[data-id="put"]')
    LOCATOR_DELETE_USER = (By.CSS_SELECTOR, '[data-id="delete"]')

class LocatorsAuthorization:
    LOCATOR_REGISTER_SUCCESSFUL = (By.CSS_SELECTOR, '[data-id="register-successful"]')
    LOCATOR_REGISTER_UNSUCCESSFUL = (By.CSS_SELECTOR, '[data-id="register-unsuccessful"]')
    LOCATOR_LOGIN_SUCCESSFUL = (By.CSS_SELECTOR, '[data-id="login-successful"]')
    LOCATOR_LOGIN_UNSUCCESSFUL = (By.CSS_SELECTOR, '[data-id="login-unsuccessful"]')
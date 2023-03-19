import json
import time
from base_app import BasePage
from locators import Locators

class SearchHelper(BasePage):

    def users(self, browser):
        search_user = self.find_element(Locators.LOCATOR_USERS)
        search_user.click()
        time.sleep(1)
        search_response_code = self.find_element(Locators.LOCATOR_RESPONSE_CODE)
        response_code = int(search_response_code.text)

        assert response_code == 200, f'Response code is - {response_code}'

        logs = browser.get_log("performance")

        url = "/api/users?page=2"
        for log in logs:
            if log["message"].startswith("{\"message\":{\"method\":\"Network.responseReceived\"") and url in log["message"]:
                request_data = json.loads(log["message"])
                status_code = request_data["message"]["params"]["response"]["status"]
                assert status_code == 200, f"The site returned the code - {status_code}, request - {request_data['message']['params']['response']['url']}"
                break

    def not_found (self, browser):
        search_not_found  = self.find_element(Locators.LOCATOR_NOT_FOUND)
        search_not_found .click()
        time.sleep(1)
        search_response_code = self.find_element(Locators.LOCATOR_RESPONSE_CODE)
        response_code = int(search_response_code.text)

        assert response_code == 404, f'Response code is - {response_code}'
        
        logs = browser.get_log("performance")
        
        url = "/api/unknown/23"
        for log in logs:
            if log["message"].startswith("{\"message\":{\"method\":\"Network.responseReceived\"") and url in log["message"]:
                request_data = json.loads(log["message"])
                status_code = request_data["message"]["params"]["response"]["status"]
                assert status_code == 404, f"The site returned the code - {status_code}, request - {request_data['message']['params']['response']['url']}"
                break

    def create_user(self, browser):
        search_create_user = self.find_element(Locators.LOCATOR_CREATE_USER)
        search_create_user.click()
        time.sleep(1)
        search_response_code = self.find_element(Locators.LOCATOR_RESPONSE_CODE)
        response_code = int(search_response_code.text)

        assert response_code == 201, f'Response code is - {response_code}'

        logs = browser.get_log("performance")

        url = "/api/users"
        for log in logs:
            if log["message"].startswith("{\"message\":{\"method\":\"Network.responseReceived\"") and url in log["message"]:
                request_data = json.loads(log["message"])
                status_code = request_data["message"]["params"]["response"]["status"]
                assert status_code == 201, f"The site returned the code - {status_code}, request - {request_data['message']['params']['response']['url']}"

    def delete_user(self, browser):
        search_delete_user = self.find_element(Locators.LOCATOR_DELETE_USER)
        search_delete_user.click()
        time.sleep(1)
        search_response_code = self.find_element(Locators.LOCATOR_RESPONSE_CODE)
        response_code = int(search_response_code.text)

        assert response_code == 204, f'Response code is - {response_code}'

        logs = browser.get_log("performance")

        url = "/api/users/2"
        for log in logs:
            if log["message"].startswith("{\"message\":{\"method\":\"Network.responseReceived\"") and url in log["message"]:
                request_data = json.loads(log["message"])
                status_code = request_data["message"]["params"]["response"]["status"]
                assert status_code == 204, f"The site returned the code - {status_code}, request - {request_data['message']['params']['response']['url']}"
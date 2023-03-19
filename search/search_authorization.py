import json
import time
from base_app import BasePage
from locators import LocatorsAuthorization, LocatorsUsers

class SearchHelper(BasePage):

    def register_pass(self, browser):
        search_register_pass = self.find_element(LocatorsAuthorization.LOCATOR_REGISTER_SUCCESSFUL)
        search_register_pass.click()
        time.sleep(2)
        search_response_code = self.find_element(LocatorsUsers.LOCATOR_RESPONSE_CODE)
        response_code = int(search_response_code.text)

        assert response_code == 200, f'Response code is - {response_code}'

        logs = browser.get_log("performance")

        url = "/api/register"
        for log in logs:
            if log["message"].startswith("{\"message\":{\"method\":\"Network.responseReceived\"") and url in log["message"]:
                request_data = json.loads(log["message"])
                status_code = request_data["message"]["params"]["response"]["status"]
                assert status_code == 200, f"The site returned the code - {status_code}, request - {request_data['message']['params']['response']['url']}"

    def register_fail(self, browser):
        search_register_fail = self.find_element(LocatorsAuthorization.LOCATOR_REGISTER_UNSUCCESSFUL)
        search_register_fail.click()
        time.sleep(2)
        search_response_code = self.find_element(LocatorsUsers.LOCATOR_RESPONSE_CODE)
        response_code = int(search_response_code.text)

        assert response_code == 400, f'Response code is - {response_code}'

        logs = browser.get_log("performance")

        url = "/api/register"
        for log in logs:
            if log["message"].startswith("{\"message\":{\"method\":\"Network.responseReceived\"") and url in log["message"]:
                request_data = json.loads(log["message"])
                status_code = request_data["message"]["params"]["response"]["status"]
                assert status_code == 400, f"The site returned the code - {status_code}, request - {request_data['message']['params']['response']['url']}"

    def login_pass(self, browser):
        search_login_pass = self.find_element(LocatorsAuthorization.LOCATOR_LOGIN_SUCCESSFUL)
        search_login_pass.click()
        time.sleep(2)
        search_response_code = self.find_element(LocatorsUsers.LOCATOR_RESPONSE_CODE)
        response_code = int(search_response_code.text)

        assert response_code == 200, f'Response code is - {response_code}'

        logs = browser.get_log("performance")

        url = "/api/login"
        for log in logs:
            if log["message"].startswith("{\"message\":{\"method\":\"Network.responseReceived\"") and url in log["message"]:
                request_data = json.loads(log["message"])
                status_code = request_data["message"]["params"]["response"]["status"]
                assert status_code == 200, f"The site returned the code - {status_code}, request - {request_data['message']['params']['response']['url']}"

    def login_fail(self, browser):
        search_login_fail = self.find_element(LocatorsAuthorization.LOCATOR_LOGIN_UNSUCCESSFUL)
        search_login_fail.click()
        time.sleep(2)
        search_response_code = self.find_element(LocatorsUsers.LOCATOR_RESPONSE_CODE)
        response_code = int(search_response_code.text)

        assert response_code == 400, f'Response code is - {response_code}'

        logs = browser.get_log("performance")

        url = "/api/login"
        for log in logs:
            if log["message"].startswith("{\"message\":{\"method\":\"Network.responseReceived\"") and url in log["message"]:
                request_data = json.loads(log["message"])
                status_code = request_data["message"]["params"]["response"]["status"]
                assert status_code == 400, f"The site returned the code - {status_code}, request - {request_data['message']['params']['response']['url']}"
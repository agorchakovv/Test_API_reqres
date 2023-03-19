import json
import time
from base_app import BasePage
from locators import LocatorsChangeUsers, LocatorsUsers

class SearchHelper(BasePage):

    def create_user(self, browser):
        search_create_user = self.find_element(LocatorsChangeUsers.LOCATOR_CREATE_USER)
        search_create_user.click()
        time.sleep(2)
        search_response_code = self.find_element(LocatorsUsers.LOCATOR_RESPONSE_CODE)
        response_code = int(search_response_code.text)

        assert response_code == 201, f'Response code is - {response_code}'

        logs = browser.get_log("performance")

        url = "/api/users"
        for log in logs:
            if log["message"].startswith("{\"message\":{\"method\":\"Network.responseReceived\"") and url and '{"name": "morpheus","job": "leader"}' in log["message"]:
                request_data = json.loads(log["message"])
                status_code = request_data["message"]["params"]["response"]["status"]
                assert status_code == 201, f"The site returned the code - {status_code}, request - {request_data['message']['params']['response']['url']}"

    def update_user(self, browser):
        search_update_user = self.find_element(LocatorsChangeUsers.LOCATOR_UPDATE_USER)
        search_update_user.click()
        time.sleep(2)
        search_response_code = self.find_element(LocatorsUsers.LOCATOR_RESPONSE_CODE)
        response_code = int(search_response_code.text)

        assert response_code == 200, f'Response code is - {response_code}'

        logs = browser.get_log("performance")

        url = "/api/users/2"
        for log in logs:
            if log["message"].startswith("{\"message\":{\"method\":\"Network.responseReceived\"") and url in log["message"]:
                request_data = json.loads(log["message"])
                status_code = request_data["message"]["params"]["response"]["status"]
                assert status_code == 200, f"The site returned the code - {status_code}, request - {request_data['message']['params']['response']['url']}"
                break

    def delete_user(self, browser):
        search_delete_user = self.find_element(LocatorsChangeUsers.LOCATOR_DELETE_USER)
        search_delete_user.click()
        time.sleep(2)
        search_response_code = self.find_element(LocatorsUsers.LOCATOR_RESPONSE_CODE)
        response_code = int(search_response_code.text)

        assert response_code == 204, f'Response code is - {response_code}'

        logs = browser.get_log("performance")

        url = "/api/users/2"
        for log in logs:
            if log["message"].startswith("{\"message\":{\"method\":\"Network.responseReceived\"") and url in log["message"]:
                request_data = json.loads(log["message"])
                status_code = request_data["message"]["params"]["response"]["status"]
                assert status_code == 204, f"The site returned the code - {status_code}, request - {request_data['message']['params']['response']['url']}"
                break
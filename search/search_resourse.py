import json
import time
from base_app import BasePage
from locators import LocatorsResourse, LocatorsUsers

class SearchHelper(BasePage):

    def list_users(self, browser):
        search_list_users= self.find_element(LocatorsResourse.LOCATOR_LIST_USERS_RESOURSE)
        search_list_users.click()
        time.sleep(2)
        search_response_code = self.find_element(LocatorsUsers.LOCATOR_RESPONSE_CODE)
        response_code = int(search_response_code.text)

        assert response_code == 200, f'Response code is - {response_code}'

        logs = browser.get_log("performance")

        url = "/api/unknown"
        for log in logs:
            if log["message"].startswith("{\"message\":{\"method\":\"Network.responseReceived\"") and url in log["message"]:
                request_data = json.loads(log["message"])
                status_code = request_data["message"]["params"]["response"]["status"]
                assert status_code == 200, f"The site returned the code - {status_code}, request - {request_data['message']['params']['response']['url']}"
                break

    def single_user(self, browser):
        search_single_user= self.find_element(LocatorsResourse.LOCATOR_SINGLE_USER_RESOURSE)
        search_single_user.click()
        time.sleep(2)
        search_response_code = self.find_element(LocatorsUsers.LOCATOR_RESPONSE_CODE)
        response_code = int(search_response_code.text)

        assert response_code == 200, f'Response code is - {response_code}'

        logs = browser.get_log("performance")

        url = "/api/unknown/2"
        for log in logs:
            if log["message"].startswith("{\"message\":{\"method\":\"Network.responseReceived\"") and url in log["message"]:
                request_data = json.loads(log["message"])
                status_code = request_data["message"]["params"]["response"]["status"]
                assert status_code == 200, f"The site returned the code - {status_code}, request - {request_data['message']['params']['response']['url']}"
                break

    def single_user_not_found(self, browser):
        search_single_user_not_found= self.find_element(LocatorsResourse.LOCATOR_SINGLE_USER_NOT_FOUND_RESOURSE)
        search_single_user_not_found.click()
        time.sleep(2)
        search_response_code = self.find_element(LocatorsUsers.LOCATOR_RESPONSE_CODE)
        response_code = int(search_response_code.text)

        assert response_code == 404, f'Response code is - {response_code}'

        logs = browser.get_log("performance")

        url = "/api/unknown/2"
        for log in logs:
            if log["message"].startswith("{\"message\":{\"method\":\"Network.responseReceived\"") and url in log["message"]:
                request_data = json.loads(log["message"])
                status_code = request_data["message"]["params"]["response"]["status"]
                assert status_code == 404, f"The site returned the code - {status_code}, request - {request_data['message']['params']['response']['url']}"
                break

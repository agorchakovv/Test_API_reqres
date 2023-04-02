import requests
import pytest
import random
import string
import json

class FuncV1:
    
    @pytest.fixture(scope="module")
    def api_url(self):
        return "https://reqres.in/api"

    @pytest.fixture(scope="function")
    def user_data_for_create(self, name_length = 10):
        letters = string.ascii_lowercase
        name = "".join(random.sample(letters, name_length))
        email = name + "@demo.com"

        data = {
            "name": name,
            "job": "tester",
            "email": email
        }

        return data
    
    @pytest.fixture(scope="function")
    def user_data_for_register(self):

        data = {
           "email": "eve.holt@reqres.in",
           "password": "pistol"
        }

        return data
    
    @pytest.fixture(scope="function")
    def user_data_for_login(self):

        data = {
           "email": "eve.holt@reqres.in",
           "password": "cityslicka"
        }

        return data

class TestApiV1(FuncV1):

    @pytest.mark.parametrize("page_num, expected_count", [(1, 6), (2, 6)])
    def test_get_list_users(self, api_url, page_num, expected_count):
        response = requests.get(f"{api_url}/users?page={page_num}")
        response_json = response.json()

        assert response.status_code == 200
        assert len(response_json["data"]) == expected_count, f"Error with len data. Print json ----- {response_json}"
        assert "support" in response_json, f"Error with support. Print json ----- {response_json}"

    @pytest.mark.parametrize("user_id, email, first_name, last_name", [(1, "george.bluth@reqres.in", "George", "Bluth"),\
                                                                       (2, "janet.weaver@reqres.in", "Janet", "Weaver")])
    def test_get_single_user(self, api_url, user_id, email, first_name, last_name):
        response = requests.get(f"{api_url}/users/{user_id}")
        response_json = response.json()

        assert response.status_code == 200
        assert response_json["data"]["email"] == email, f"Error with email. Print json ----- {response_json}"
        assert response_json["data"]["first_name"] == first_name, f"Error with first_name. Print json ----- {response_json}"
        assert response_json["data"]["last_name"] == last_name, f"Error with last_name. Print json ----- {response_json}"

    @pytest.mark.parametrize("user_id", [(23)])
    def test_get_single_user_not_found(self, api_url, user_id):
        response = requests.get(f"{api_url}/users/{user_id}")

        assert response.status_code == 404

    @pytest.mark.parametrize("expected_count", [(6)])
    def test_get_list_resourse(self, api_url, expected_count):
        response = requests.get(f"{api_url}/unknown")
        response_json = response.json()

        assert response.status_code == 200
        assert len(response_json["data"]) == expected_count, f"Error with len data. Print json ----- {response_json}"
        assert "support" in response_json, f"Error with support. Print json ----- {response_json}"

    @pytest.mark.parametrize("user_id, name, year", [(1, "cerulean", "2000"),\
                                                     (2, "fuchsia rose", "2001")])
    def test_get_single_resourse(self, api_url, user_id, name, year):
        response = requests.get(f"{api_url}/unknown/{user_id}")
        response_json = response.json()

        assert response.status_code == 200
        assert response_json["data"]["name"] == name, f"Error with name. Print json ----- {response_json}"
        assert response_json["data"]["year"] == int(year), f"Error with year. Print json ----- {response_json}"

    @pytest.mark.parametrize("user_id", [(23)])
    def test_get_single_resourse_not_found(self, api_url, user_id):
        response = requests.get(f"{api_url}/unknown/{user_id}")

        assert response.status_code == 404

    def test_post_create_user(self, api_url, user_data_for_create):
        data = user_data_for_create
        response = requests.post(f"{api_url}/users", data)
        response_json = response.json()

        assert response.status_code == 201
        assert response_json["name"] == data["name"], f"Error with name. Print json ----- {response_json}"
        assert response_json["job"] == data["job"], f"Error with job. Print json ----- {response_json}"
        assert response_json["email"] == data["email"], f"Error with email. Print json ----- {response_json}"

    @pytest.mark.parametrize("user_id", [(1), (2)])
    def test_put_update_user(self, api_url, user_data_for_create, user_id):
        data = user_data_for_create
        response = requests.put(f"{api_url}/users/{user_id}", data)
        response_json = response.json()

        assert response.status_code == 200
        assert response_json["name"] == data["name"], f"Error with name. Print json ----- {response_json}"
        assert response_json["job"] == data["job"], f"Error with job. Print json ----- {response_json}"

    @pytest.mark.parametrize("user_id", [(1), (2)])
    def test_delete_user(self, api_url, user_id):
        response = requests.delete(f"{api_url}/users/{user_id}")

        assert response.status_code == 204

    def test_post_register(self, api_url, user_data_for_register):
        data = user_data_for_register
        response = requests.post(f"{api_url}/register", data)
        response_json = response.json()

        assert response.status_code == 200
        assert "token" in response_json, f"Error with token. Print json ----- {response_json}"
        assert response.json()["token"] != "", f"Token is null. Print json ----- {response_json}"

    def test_post_register_unsuccsesful(self, api_url, user_data_for_register):
        data = {"email": user_data_for_register["email"]}
        response = requests.post(f"{api_url}/register", data)
        response_json = response.json()

        assert response.status_code == 400
        assert "error" in response_json, f"Error with key error. Print json ----- {response_json}"
        assert response_json["error"] == "Missing password", f"Error with value key error. Print json ----- {response_json}"

    def test_post_login(self, api_url, user_data_for_login):
        data = user_data_for_login
        response = requests.post(f"{api_url}/login", data)
        response_json = response.json()

        assert response.status_code == 200
        assert "token" in response_json, f"Error with token. Print json ----- {response_json}"
        assert response_json["token"] != "", f"Token is null. Print json ----- {response_json}"

    def test_post_login_unseccsesful(self, api_url, user_data_for_login):
        data = {"email": user_data_for_login["email"]}
        response = requests.post(f"{api_url}/login", data)
        response_json = response.json()

        assert response.status_code == 400
        assert "error" in response_json, f"Error with key error. Print json ----- {response_json}"
        assert response_json["error"] == "Missing password", f"Error with value key error. Print json ----- {response_json}"


    @pytest.mark.parametrize("expected_count", [(6)])
    def test_delayed_response_get_list_users(self, api_url, expected_count):
        response = requests.get(f"{api_url}/users?delay=3")
        response_json = response.json()

        assert response.status_code == 200
        assert len(response_json["data"]) == expected_count, f"Error with len data. Print json ----- {response_json}"
        assert "support" in response_json, f"Error with support. Print json ----- {response_json}"
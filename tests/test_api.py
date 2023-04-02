import requests
import pytest
import random
import string

class FuncV1:
    
    @pytest.fixture(scope="module")
    def api_url(self):
        return "https://reqres.in/api"

    @pytest.fixture(scope="function")
    def user_data(self, name_length=10):
        letters = string.ascii_lowercase
        name = ''.join(random.sample(letters, name_length))
        email = name + "@demo.com"

        data = {
            "name": name,
            "job": "tester",
            "email": email
        }

        return data

class TestApiV1(FuncV1):

    @pytest.mark.parametrize("page_num, expected_count", [(1, 6), (2, 6)])
    def test_get_list_users(self, api_url, page_num, expected_count):
        response = requests.get(f"{api_url}/users?page={page_num}")
        json = response.json()

        assert response.status_code == 200
        assert len(response.json()["data"]) == expected_count, f"Print json ----- {json}"
        assert "support" in response.json(), f"Print json ----- {json}"

    @pytest.mark.parametrize("user_id, email, first_name, last_name", [(1, "george.bluth@reqres.in", "George", "Bluth"),\
                                                                    (2, "janet.weaver@reqres.in", "Janet", "Weaver")])
    def test_get_single_user(self, api_url, user_id, email, first_name, last_name):
        response = requests.get(f"{api_url}/users/{user_id}")

        assert response.status_code == 200
        assert response.json()["data"]["email"] == email
        assert response.json()["data"]["first_name"] == first_name
        assert response.json()["data"]["last_name"] == last_name

    @pytest.mark.parametrize("user_id", [(23)])
    def test_get_single_user_not_found(self, api_url, user_id):
        response = requests.get(f"{api_url}/users/{user_id}")

        assert response.status_code == 404

    def test_post_create_user(self, api_url, user_data):
        data=user_data
        response = requests.post(f"{api_url}/users", data=data)

        assert response.status_code == 201
        assert response.json()["name"] == user_data["name"]
        assert response.json()["job"] == user_data["job"]
        assert response.json()["email"] == user_data["email"]

    @pytest.mark.parametrize("user_id", [(1), (2)])
    def test_put_update_user(self, api_url, user_data, user_id):
        data=user_data
        response = requests.put(f"{api_url}/users/{user_id}", data=data)

        assert response.status_code == 200
        assert response.json()["name"] == user_data["name"]
        assert response.json()["job"] == user_data["job"]

    @pytest.mark.parametrize("user_id", [(1), (2)])
    def test_delete_user(self, api_url, user_id):
        response = requests.delete(f"{api_url}/users/{user_id}")

        assert response.status_code == 204

    def test_not_found(self, api_url):
        response = requests.get(f"{api_url}/unknown/23")

        assert response.status_code == 404
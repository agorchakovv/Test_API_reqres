import requests
import pytest

@pytest.fixture(scope="session")
def api_url():
    return "https://reqres.in/api"

@pytest.mark.parametrize("page_num, expected_count", [(1, 6), (2, 6)])
def test_list_users(api_url, page_num, expected_count):
    response = requests.get(f"{api_url}/users?page={page_num}")
    json = response.json()
    assert response.status_code == 200
    assert len(response.json()["data"]) == expected_count, f"Print json ----- {json}"
    assert "support" in response.json(), f"Print json ----- {json}"

@pytest.mark.parametrize("user_id, email, first_name, last_name", [(1, "george.bluth@reqres.in", "George", "Bluth"), (2, "janet.weaver@reqres.in", "Janet", "Weaver")])
def test_get_single_user(api_url, user_id, email, first_name, last_name):
    response = requests.get(f"{api_url}/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["data"]["email"] == email
    assert response.json()["data"]["first_name"] == first_name
    assert response.json()["data"]["last_name"] == last_name

@pytest.mark.parametrize("user_id", [(23)])
def test_single_user_not_found(api_url, user_id):
    response = requests.get(f"{api_url}/users/{user_id}")
    assert response.status_code == 404

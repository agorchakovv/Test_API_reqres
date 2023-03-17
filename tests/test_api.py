import requests
import pytest

@pytest.fixture(scope="session")
def api_url():
    return "https://reqres.in/api"

def test_list_users(api_url):
    response = requests.get(f"{api_url}/users?page=1")
    json = response.json()
    assert response.status_code == 200
    assert len(response.json()["data"]) == 6, f"Print json ----- {json}"
    assert "support" in response.json(), f"Print json ----- {json}"

# def test_get_single_user():
#     response = requests.get("https://reqres.in/api/users/2")
#     assert response.status_code == 200
#     assert response.json()["data"]["email"] == "janet.weaver@reqres.in"
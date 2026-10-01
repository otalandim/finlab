import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_agent_endpoint_apple():
    response = requests.get(f"{BASE_URL}/users")

    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

    print(data[0])

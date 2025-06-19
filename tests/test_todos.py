import requests
import pytest

base_url = "https://jsonplaceholder.typicode.com"

def test_get_todo():
    response = requests.get(f"{base_url}/todos/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "title" in data

def test_create_todo():
    payload = {
        "userId": 1,
        "title": "Learn API Testing with Python",
        "completed": False
    }
    response = requests.post(f"{base_url}/todos", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]

def test_update_todo():
    payload = {
        "userId": 1,
        "title": "Updated Title",
        "completed": True
    }
    response = requests.put(f"{base_url}/todos/1", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Title"

def test_delete_todo():
    response = requests.delete(f"{base_url}/todos/1")
    assert response.status_code in [200, 204]

@pytest.mark.parametrize("payload, expected_status", [
    ({}, 201),
    ({"userId": "abc", "title": "", "completed": "notbool"}, 201),
    (None, 201),
])
def test_create_todo_invalid_data(payload, expected_status):
    response = requests.post(f"{base_url}/todos", json=payload)
    assert response.status_code == expected_status

@pytest.mark.parametrize("user_id, title, completed", [
    (1, "Learn API Testing", False),
    (2, "Write test cases", True),
    (3, "Fix bugs", False),
])
def test_create_todo_param(user_id, title, completed):
    payload = {
        "userId": user_id,
        "title": title,
        "completed": completed
    }
    response = requests.post(f"{base_url}/todos", json=payload)
    assert response.status_code == 201
    json_data = response.json()
    assert json_data["userId"] == user_id
    assert json_data["title"] == title
    assert json_data["completed"] == completed

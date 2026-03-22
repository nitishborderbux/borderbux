from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post(
        "/v1/users/create",
        json={"full_name": "John Doe", "email": "john@example.com", "password": "secret"}
    )
    assert response.status_code == 200
    assert response.json()["full_name"] == "John Doe"

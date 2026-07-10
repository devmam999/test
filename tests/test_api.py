from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_login_and_profile() -> None:
    login_response = client.post(
        "/login",
        json={
            "username": "demo",
            "password": "password123",
        },
    )

    assert login_response.status_code == 200

    token = login_response.json()["access_token"]

    profile_response = client.get(
        "/profile",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert profile_response.status_code == 200
    assert profile_response.json()["username"] == "demo"
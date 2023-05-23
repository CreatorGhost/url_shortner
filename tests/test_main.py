import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_hash_url():
    response = client.post(
        "/hash-url", 
        json={"url": "https://www.youtube.com/watch?v=AEE9ecgLgdQ&ab_channel=PatrickLoeber", "single_use": False}
    )
    assert response.status_code == 200
    assert "url" in response.json()


def test_redirect_url():
    # First, create a short url
    response = client.post(
        "/hash-url", 
        json={"url": "https://www.example.com", "single_use": False}
    )
    short_url = response.json()["url"]

    # Then, use it for redirection
    response = client.get(f"/redirect?hashed_url={short_url}")
    assert response.status_code == 200
    assert response.json()["url"] == "https://www.example.com"


def test_get_clicks():
    # First, create a short url
    response = client.post(
        "/hash-url", 
        json={"url": "https://www.example.com", "single_use": False}
    )
    short_url = response.json()["url"]

    # Then, use it to get clicks
    response = client.get(f"/clicks?short_url={short_url}")
    assert response.status_code == 200
    assert response.json()["click_count"] == 0

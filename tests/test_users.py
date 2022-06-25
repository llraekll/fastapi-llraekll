from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.main import app


client=TestClient(app)

def test_root():
    res = client.get("/")
    print(res.json().get('message'))
    assert res.json().get('message') == 'Hello human!'
    assert res.status_code == 200

def test_create_user():
    res = client.post(
        "/users/", json={"email": "test@yahoo.in", "password": "random"})
    print(res.json())
    assert res.json().get("email") == "test@yahoo.in"
    assert res.status_code == 201
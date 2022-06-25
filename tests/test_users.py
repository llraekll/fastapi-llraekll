from app import schemas
from .database import client, session


def test_root(client):
    res = client.get("/")
    print(res.json().get('message'))
    assert res.json().get('message') == 'Hello human!'
    assert res.status_code == 200

def test_create_user(client):
    res = client.post(
        "/users/", json={"email": "testone@yahoo.in", "password": "random"})
    new_user=schemas.UserOut(**res.json())
    assert new_user.email == "testone@yahoo.in"
    assert res.status_code == 201
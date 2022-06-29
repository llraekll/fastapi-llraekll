from urllib import response
from jose import jwt
import pytest
from app import schemas
from app.config import settings



def test_root(client):
    res = client.get("/")
    print(res.json().get('message'))
    assert 1==1
    assert res.json().get('message') == 'Hello human!'
    assert res.status_code == 200

def test_create_user(client):
    res = client.post(
        "/users/", json={"email": "testone@yahoo.in", "password": "random"})
    new_user=schemas.UserOut(**res.json())
    assert new_user.email == "testone@yahoo.in"
    assert res.status_code == 201

def test_login_user(client, test_user):
    res = client.post(
        "/login", data={"username": test_user['email'], "password": test_user['password']})
    login_res = schemas.Token(**res.json())
    payload= jwt.decode(login_res.access_token, settings.secret_key, settings.algorithm)
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200

@pytest.mark.parametrize("email, password, status_code",[
    ('testone@yahoo.in', 'wrong', 403),
    ('wrong@mail.com', 'random', 403),
    ('testone@yahoo.in', 'wrong', 403),
    ('testone@yahoo.in', None, 422),
    (None, 'random', 422)
])
def test_incorrect_login(test_user, client, email, password, status_code):
    res = client.post("/login", data={"username": email, "password":password})
    assert res.status_code == status_code
    # assert res.json().get('detail') == 'Invaild Credentials' 


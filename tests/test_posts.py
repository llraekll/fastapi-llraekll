from requests import post
from app import schemas
from typing import List
import pytest

def test_get_all_posts(authorized_client, test_posts):
    res= authorized_client.get("/posts/")
    def validate(post):
        return schemas.PostOut(**post)
    posts_map = map(validate, res.json())
    posts_list = list(posts_map)
    print(list(posts_map))

    assert len(res.json()) == len(test_posts)
    assert res.status_code == 200
    #assert posts_list[0].Post.id == test_posts[0].id

def test_unauthorised_user_get_all_posts(client, test_posts):
    res = client.get('/posts/')
    assert res.status_code == 401

def test_unauthorised_user_get_one_post(client, test_posts):
    res = client.get("/posts/{test_posts[0].id}")
    assert res.status_code == 401

def test_get_one_post_not_exist(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/82973")
    assert res.status_code == 404

def test_get_one_post(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/{test_posts[0].id}")
    post = schemas.PostOut(**res.json())
    assert post.Post.id == test_posts[0].id
    assert post.Post.content == test_posts[0].content

@pytest.mark.parametrize("title, content, published",[
    ("sometitle", "random content", True),
    ("food", "It's too good", True),
    ("Favourite food", "You know what you like", False)
])
def test_create_post(authorized_client, test_posts, test_user, title, content, published):
    res = authorized_client.post("/posts/", json={"title": title, "content": content, "published": published})
    created_post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_post.title == title
    assert created_post.content == content
    assert created_post.published == published
    assert created_post.owner_id == test_user['id']

def test_create_post_default_published_true(authorized_client, test_user, test_posts):
    res = authorized_client.post("/posts/", json={"title": "dskfh", "content": "dksfg"})
    created_post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_post.title == "dskfh"
    assert created_post.content == "dksfg"
    assert created_post.published == True
    assert created_post.owner_id == test_user['id']

def test_unauthorised_user_create_post(client, test_posts):
    res = client.post("/posts/", json={"title": "dskfh", "content": "dksfg"})
    assert res.status_code == 401

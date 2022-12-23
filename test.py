import pytest as pytest
from app import app

@pytest.fixture()
def client():
    return app.test_client()

@pytest.fixture()
def post_keys():
    return {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

def testing_api_posts(client, post_keys):
    response = client.get('/api/posts')
    assert response.status_code == 200
    assert type(response.json) == list
    for element in response.json:
        assert element.keys() == post_keys

def testing_api_post(client, post_keys):
    response = client.get('/api/post/1')
    assert response.status_code == 200
    assert type(response.json) == dict
    assert response.json.keys() == post_keys

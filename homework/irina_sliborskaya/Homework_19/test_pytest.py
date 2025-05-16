import requests
import pytest


@pytest.fixture(scope='session')
def session_period():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture(scope='function')
def each_test_period():
    print('before test')
    yield
    print(' after test')


@pytest.fixture()
def new_object_id():
    body = {
        "name": "ISL object 2",
        "data": {
            "color": "yellow",
            "size": "mid"
        }
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        "http://167.172.172.115:52353/object",
        json=body,
        headers=headers
    )
    object_id = response.json()['id']
    yield object_id
    requests.delete(f"http://167.172.172.115:52353/object/{new_object_id}")


@pytest.mark.critical
@pytest.mark.parametrize('json', [
    '{"name": "ISL object 2","data": {"color": "yellow","size": "111"}}',
    ' {"name": "ISL object 2","data": {"color": "blue","size": "222"}}',
    '{"name": "ISL object 2","data": {"color": "white","size": "333"}}'
])
def test_post_an_object(session_period, each_test_period, json):
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        "http://167.172.172.115:52353/object",
        json,
        headers=headers
    )
    assert response.status_code == 200, "Object wasn't created"


def test_put_an_object(new_object_id, each_test_period):
    body = {
        "name": "ISL object 222",
        "data": {
            "color": "blue",
            "size": "mid"
        }
    }
    headers = {"Content-Type": "application/json"}
    response = requests.put(
        f"http://167.172.172.115:52353/object/{new_object_id}",
        json=body,
        headers=headers
    )
    assert response.json()['name'] == "ISL object 222", 'Incorrect name of object'
    assert response.json()['data']['color'] == "blue", 'Incorrect color'


def test_patch_an_object(new_object_id, each_test_period):
    body = {
        "data": {
            "color": "yellow",
            "size": "small"
        }
    }
    headers = {"Content-Type": "application/json"}
    response = requests.patch(
        f"http://167.172.172.115:52353/object/{new_object_id}",
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['data']['size'] == "small", 'Incorrect size'


@pytest.mark.medium
def test_delete_an_object(new_object_id, each_test_period):
    response = requests.delete(f"http://167.172.172.115:52353/object/{new_object_id}")
    assert response.status_code == 200, 'Delete action is not successful'

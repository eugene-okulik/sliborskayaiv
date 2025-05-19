import pytest
import requests


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

import requests


def post_an_object():
    body = {
        "name": "ISL object",
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
    assert response.json()['name'] == "ISL object", 'Incorrect name of object'
    assert response.json()['data']['color'] == "yellow", 'Incorrect color'


def new_post():
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
    return response.json()['id']


def clear(post_id):
    requests.delete(f"http://167.172.172.115:52353/object/{post_id}")


def put_an_object():
    post_id = new_post()
    body = {
        "name": "ISL object 222",
        "data": {
            "color": "blue",
            "size": "mid"
    }
    }
    headers = {"Content-Type": "application/json"}
    response = requests.put(
        f"http://167.172.172.115:52353/object/{post_id}",
        json=body,
        headers=headers
    )
    assert response.json()['name'] == "ISL object 222", 'Incorrect name of object'
    assert response.json()['data']['color'] == "blue", 'Incorrect color'
    clear(post_id)


def patch_an_object():
    post_id = new_post()
    body = {
        "data": {
            "color": "yellow",
            "size": "small"
    }
    }
    headers = {"Content-Type": "application/json"}
    response = requests.patch(
        f"http://167.172.172.115:52353/object/{post_id}",
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['data']['size'] == "small", 'Incorrect size'
    clear(post_id)


def delete_an_object():
    post_id = new_post()
    response = requests.delete(f"http://167.172.172.115:52353/object/{post_id}")
    assert response.status_code == 200, 'Delete action is not successful'


post_an_object()
put_an_object()
patch_an_object()
delete_an_object()

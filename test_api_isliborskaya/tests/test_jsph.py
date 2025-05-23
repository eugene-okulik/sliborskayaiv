import pytest


opt = [
    {"name": "ISL object 3", "data": {"color": "yellow", "size": "111"}},
    {"name": "ISL object 2", "data": {"color": "blue", "size": "222"}},
    {"name": "ISL object 1", "data": {"color": "new", "size": "333"}}
]


@pytest.mark.parametrize('test_data', opt)
def test_post_an_object(create_object_endpoint, test_data, delete_object_endpoint):
    create_object_endpoint.new_object(payload=test_data)
    create_object_endpoint.check_status_is_200()
    create_object_endpoint.check_response_name_is_correct(test_data['name'])
    create_object_endpoint.check_response_color_is_correct(test_data["data"]["color"])
    object_id = create_object_endpoint.json['id']
    delete_object_endpoint.delete_object(object_id)


def test_put_an_object(update_object_endpoint, create_object_endpoint, delete_object_endpoint):
    payload = {"name": "ISL object PUT", "data": {"color": "yellow", "size": "555"}}
    create_object_endpoint.new_object(payload)
    object_id = create_object_endpoint.json['id']
    payload_to_test = {"name": "ISL object PUT edited", "data": {"color": "blue", "size": "555"}}
    update_object_endpoint.make_changes_in_object(object_id, payload_to_test)
    update_object_endpoint.check_status_is_200()
    update_object_endpoint.check_response_name_is_correct(payload_to_test['name'])
    update_object_endpoint.check_response_color_is_correct(payload_to_test["data"]["color"])
    delete_object_endpoint.delete_object(object_id)


def test_patch_an_object(update_object_endpoint, create_object_endpoint, delete_object_endpoint):
    payload = {"name": "ISL object PATCH", "data": {"color": "yellow", "size": "555"}}
    create_object_endpoint.new_object(payload)
    object_id = create_object_endpoint.json['id']
    payload_to_test = {"data": {"color": "new", "size": "PATCH"}}
    update_object_endpoint.patch_object(object_id, payload_to_test)
    update_object_endpoint.check_status_is_200()
    update_object_endpoint.check_response_color_is_correct(payload_to_test["data"]["color"])
    delete_object_endpoint.delete_object(object_id)


def test_delete_an_object(delete_object_endpoint, create_object_endpoint):
    payload = {"name": "ISL object TEST", "data": {"color": "yellow", "size": "555"}}
    create_object_endpoint.new_object(payload)
    object_id = create_object_endpoint.json['id']
    delete_object_endpoint.delete_object(object_id)
    delete_object_endpoint.check_status_is_200()

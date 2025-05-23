import pytest
from test_api_isliborskaya.endpoints.create_object import CreateObject
from test_api_isliborskaya.endpoints.delete_object import DeleteObject
from test_api_isliborskaya.endpoints.update_object import UpdateObject
import sys
import os


sys.path.append(os.path.abspath(os.path.dirname(__file__)))

@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()

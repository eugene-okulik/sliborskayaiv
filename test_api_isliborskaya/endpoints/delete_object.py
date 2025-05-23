import requests
import allure
from test_api_isliborskaya.endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):


    @allure.step('Delete an object')
    def delete_object(self, object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(
            f'{self.url}/{object_id}',
            headers=headers
        )
        try:
            if self.response.text:
                self.json = self.response.json()
            else:
                self.json = None
        except ValueError:
            self.json = None
        return self.response

import allure


class Endpoint:
    url = "http://167.172.172.115:52353/object"
    response = None
    json = None
    headers = {"Content-Type": "application/json"}

    @allure.step('Check that name is the same as sent')
    def check_response_name_is_correct(self, name):
        assert self.json['name'] == name

    @allure.step('Check that COLOR is the same as sent')
    def check_response_color_is_correct(self, color):
        assert self.json['data']['color'] == color

    @allure.step('Check that response is 200')
    def check_status_is_200(self):
        assert self.response.status_code == 200

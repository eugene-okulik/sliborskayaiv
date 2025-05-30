from locust import task, HttpUser
import random


class ObjectUser(HttpUser):
    object_id = None

    @task(1)
    def get_all_objects(self):
        self.client.get(
            '/object',
            headers={"Content-Type": "application/json"}
        )

    @task(3)
    def get_one_object(self):
        random_id = random.randint(1, 100)
        self.client.get(
            f'/object/{random_id}'
        )

    @task
    def post_one_object(self):
        response = self.client.post(
            '/object',
            json={"name": "ISL object 3", "data": {"color": "yellow", "size": "111"}},
            headers={"Content-Type": "application/json"}
        )
        self.object_id = response.json()['id']
        self.client.delete(
            f'/object/{self.object_id}'
        )

    @task
    def put_object(self):
        create_test_obj = self.client.post(
            '/object',
            json={"name": "ISL object 3", "data": {"color": "yellow", "size": "111"}},
            headers={"Content-Type": "application/json"}
        )
        self.object_id = create_test_obj.json()['id']
        self.client.put(
            f'/object/{self.object_id}',
            json={"name": "Edited", "data": {"color": "yellow", "size": "222"}},
            headers={"Content-Type": "application/json"}
        )
        self.client.delete(
            f'/object/{self.object_id}'
        )

    @task
    def patch_object(self):
        create_test_obj = self.client.post(
            '/object',
            json={"name": "ISL object 3", "data": {"color": "yellow", "size": "111"}},
            headers={"Content-Type": "application/json"}
        )
        self.object_id = create_test_obj.json()['id']
        self.client.patch(
            f'/object/{self.object_id}',
            json={"data": {"color": "blue", "size": "333"}},
            headers={"Content-Type": "application/json"}
        )
        self.client.delete(
            f'/object/{self.object_id}'
        )

    @task
    def delete_object(self):
        create_test_obj = self.client.post(
            '/object',
            json={"name": "ISL object 3", "data": {"color": "yellow", "size": "111"}},
            headers={"Content-Type": "application/json"}
        )
        self.object_id = create_test_obj.json()['id']
        self.client.delete(
            f'/object/{self.object_id}'
        )

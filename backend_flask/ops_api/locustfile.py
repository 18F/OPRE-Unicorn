from locust import between
from locust import HttpUser
from locust import task


class CanUser(HttpUser):

    wait_time = between(1, 5)

    @task
    def can_list(self):
        self.client.get("/ops/cans")

    @task
    def can_detail(self):
        self.client.get("/ops/cans/1")

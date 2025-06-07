from locust import HttpUser, between, task, TaskSet
import threading

TARGET_HOST = "http://127.0.0.1:8000"

TOTAL_REQUESTS = 200
request_counter = 0
counter_lock = threading.Lock()


class CounterTasks(TaskSet):
    wait_time = between(0.1, 0.5)

    @task
    def increment_counter_in_set(self):

        global request_counter
        with counter_lock:
            if request_counter >= TOTAL_REQUESTS:
                print(request_counter)
                self.interrupt()
            request_counter += 1

        self.client.post("/api/counter/")


class CounterUserWithTaskSet(HttpUser):
    host = TARGET_HOST
    tasks = [CounterTasks]

from locust import HttpUser, between, task

# 테스트할 웹 서버의 주소
# 여기에 최지웅1822님이 부하 테스트할 로컬 서버 주소를 넣어줘!
TARGET_HOST = "http://127.0.0.1:8000"

# 사용자의 행동을 정의하는 클래스


class WebsiteUser(HttpUser):
    # 테스트할 대상 주소 설정
    host = TARGET_HOST

    # 사용자가 각 작업을 수행한 후 대기하는 시간 (초 단위)
    # 여기서는 1초에서 5초 사이로 랜덤하게 대기해!
    wait_time = between(1, 5)

    # @task 데코레이터를 붙인 메서드가 사용자가 수행할 작업이야!
    # 여기에 아무런 숫자 (가중치)를 안 붙이면 똑같은 확률로 실행돼.
    @task
    def access_root(self):
        # self.client는 HttpUser가 제공하는 HTTP 클라이언트 객체야.
        # 이걸로 GET, POST 같은 HTTP 요청을 보낼 수 있지!
        # 여기서는 루트 경로('/')로 GET 요청을 보내는 작업!
        print("Accessing root page...")  # 터미널에 뭔가 찍히는 걸 보고 싶으면 이렇게 넣어줘!
        self.client.get("/")
        print("Finished accessing root page.")  # 요청이 끝났을 때

    # 만약 다른 페이지에도 접속하는 걸 시뮬레이션하고 싶으면 이렇게 @task 메서드를 더 추가하면 돼!
    # @task
    # def access_about(self):
    #     print("Accessing about page...")
    #     self.client.get("/about")
    #     print("Finished accessing about page.")

    # 만약 특정 API 엔드포인트에 요청을 보내고 싶으면 이렇게!
    # @task
    # def call_api_users(self):
    #     print("Calling /api/users...")
    #     self.client.get("/api/users")
    #     print("Finished calling /api/users.")

    # POST 요청 보내는 예시 (데이터와 함께)
    # @task
    # def create_user(self):
    #     print("Creating a user...")
    #     user_data = {"username": "testuser", "password": "testpassword"}
    #     # json=user_data 처럼 딕셔너리로 넘기면 자동으로 JSON으로 변환해서 Content-Type 헤더도 설정해줘!
    #     self.client.post("/api/users", json=user_data)
    #     print("Finished creating a user.")

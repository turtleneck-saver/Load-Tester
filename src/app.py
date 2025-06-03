from locust import HttpUser, between, task
import json  # 응답으로 받은 JSON 데이터를 파싱하기 위해 필요해!

# 테스트할 웹 서버의 주소
TARGET_HOST = "http://127.0.0.1:8000"

# 사용자의 행동을 정의하는 클래스


class CounterUser(HttpUser):  # 클래스 이름을 좀 더 명확하게 'CounterUser'로 바꿔봤어!
    # 테스트할 대상 주소 설정
    host = TARGET_HOST

    # 사용자가 각 작업을 수행한 후 대기하는 시간 (초 단위)
    # 여기서는 0.5초에서 2초 사이로 랜덤하게 대기해볼까?
    wait_time = between(1, 1)

    # @task 데코레이터를 붙인 메서드가 사용자가 수행할 작업이야!
    # 여기서는 POST 요청을 보내서 카운터를 1 증가시키는 작업!
    @task
    def increment_counter_and_check(self):
        print("Sending POST request to increment counter...")

        # 카운터 증가 API 엔드포인트로 POST 요청 보내기!
        # POST 요청이라 본문에 데이터를 보낼 수도 있지만,
        # 이 API는 본문 데이터 없이도 작동하니까 그냥 보낼게!
        response = self.client.post("/api/counter/")

        # 요청 성공 (HTTP 상태 코드 200)인지 확인!
        if response.status_code == 200:
            print("POST request successful!")
            try:
                # 응답으로 받은 JSON 데이터 파싱
                result = response.json()
                # 파싱된 데이터에서 'count' 값을 가져와서 출력!
                # .get() 사용해서 키 없어도 에러 안 나게!
                print(f"Received increased count: {result.get('count')}")

                # 만약 현재 카운트 값을 GET으로 확인하고 싶다면 여기서 추가 요청을 보낼 수도 있어!
                # print("Sending GET request to check current count...")
                # get_response = self.client.get("/api/counter/")
                # if get_response.status_code == 200:
                #    get_result = get_response.json()
                #    print(f"Current count from GET: {get_result.get('count')}")

            except json.JSONDecodeError:
                print("Error decoding JSON response.")
            except Exception as e:
                print(f"An error occurred while processing response: {e}")
        else:
            # 요청 실패 시 상태 코드 출력!
            print(
                f"POST request failed with status code: {response.status_code}")
            # 실패 시 응답 내용도 확인해보면 좋아!
            print(f"Response content: {response.text}")


# ⚠️ 만약 GET 요청만 보내는 사용자도 시뮬레이션하고 싶다면 다른 클래스를 만들어줘!

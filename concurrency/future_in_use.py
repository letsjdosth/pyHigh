from concurrent.futures import Future
import threading
# 실상 콜백의 래퍼임. 하지만 콜백과의 비교- 장점이 있음
# 1. 가독성(콜백 지옥 x)
# 2. 쉬운 에러처리 및 전파 (콜백의 끔찍한 에러 전파와 비교...)
# 3. 작업 상태 추적 (대기?종료?) 및 제어 (취소 가능 등)

def network_request_async(number):
    future = Future()
    result = {"success": True, "result": number**2}
    timer = threading.Timer(1.0, lambda: future.set_result(result))
    timer.start()
    return future

def fetch_square(number):
    fut = network_request_async(number)

    def on_done_future(future):
        response = future.result()
        if response["success"]:
            print("Result is: {}".format(response["result"]))

    fut.add_done_callback(on_done_future)

print("<start>")
fetch_square(2)
fetch_square(3)
fetch_square(4)
print("<after submitions>")
# <start>
# <after submitions>
# Result is: 4
# Result is: 16
# Result is: 9
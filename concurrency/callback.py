# 콜백
# 비동기 실행 이후 작업시, 특성상 main으로의 리턴을 못 하므로
# 해당 함수 이후 호출될 함수인 콜백을 넘겨서 작업을 마저 돌린다.

import threading
import time

def wait_and_print_async(msg):
    def callback():
        print(msg)
    timer = threading.Timer(1.0, callback) #threading.timer는 비동기로 돌아간다
    timer.start()

def network_request_async(number, on_done): 
    # 비동기함수에서는 리턴을 받을 수 없기 때문에, 이후 작업을 콜백으로 넘긴다
    def timer_done():
        on_done({
            "success": True,
            "result" : number**2
        })
    timer = threading.Timer(1.0, timer_done)
    timer.start()

def on_done_print(result):
    print(result)

def fetch_square(number):
    def on_done_print_if_success(response):
        if response["success"]:
            print("Result is: {}".format(response["result"]))
    network_request_async(number, on_done_print_if_success)

if __name__=="__main__":
    wait_and_print_async("First call async")
    wait_and_print_async("Second call async")
    print("<wait...>")
# <wait...>
# First call async
# Second call async

    time.sleep(1.5)
    network_request_async(2, on_done_print)
    network_request_async(3, on_done_print)
    network_request_async(4, on_done_print)
    print("after submition...")
# after submition...
# {'success': True, 'result': 4}
# {'success': True, 'result': 9}
# {'success': True, 'result': 16}

    time.sleep(1.5)
    fetch_square(2)
    fetch_square(3)
    fetch_square(4)
    print("after submition...")
# after submition...
# Result is: 4
# Result is: 9
# Result is: 16
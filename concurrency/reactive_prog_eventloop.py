# event 기반 프로그래밍
# main은 event 발생을 계속 모니터링하다가, 발생시 특정 작업을 처리
# 혹은 들어오는 작업을 시분할해 끼워 처리

import time

class Timer:
    def __init__(self, timeout):
        self.timeout = timeout
        self.start = time.time()
    
    def done(self):
        return (time.time() - self.start) > self.timeout
    
    def on_time_done(self, callback):
        self.callback = callback

timer1 = Timer(1.0)
timer1.on_time_done(lambda: print("First timer is done!"))

timer2 = Timer(2.0)
timer2.on_time_done(lambda: print("Second timer is done!"))

timers_work_list = [] #할일 list 대용 역할. 
timers_work_list.append(timer1) #(이벤트 발생시 위 할일 큐 혹은 리스트에 할 일이 푸시됨)
timers_work_list.append(timer2)

# ~main~ event loop
# 패러다임상의 중요점: 일하는 함수는 루프에서 명시적으로 직접 호출한다.
# (클래스 내 함수도, 직접 접근해 호출하자)
if __name__ == "__main__":
    while(True):
        for timer in timers_work_list:
            if timer.done():
                timer.callback()
                timers_work_list.remove(timer) #해당 일 다 하면 할일 큐/리스트에서 해당 요소 빼자
        
        if len(timers_work_list)==0:
            print("program finished!") 
            break

# First timer is done!
# Second timer is done!
# program finished!
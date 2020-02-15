from concurrent import futures
# Future
# 구조 구경
# (실제 코드에서는 직접 생성하지 말 것)
fut = futures.Future()
print(fut) # <Future at 0x1a88c653888 state=pending> #<- state를 가지고있다. 현재 대기중(사용불가)

fut.set_result("Hello")
print(fut) # <Future at 0x1a88c653888 state=finished returned str> #<- 입력이 있었고 이제 사용가능 상태. str임까지 보여줌
result = fut.result() #<-리턴해올 수 있음
print(result) # Hello

# 퓨처에 콜백 등록
def test_callback(fut_inst):
    print("future finished! result: " + fut_inst.result(), flush=True)

fut2 = futures.Future()
fut2.add_done_callback(test_callback)
fut2.set_result("Hi!")
# future finished! result: Hi!


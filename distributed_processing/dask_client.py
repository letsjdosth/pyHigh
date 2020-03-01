# 미리 설정된 기반 스케줄러 : 워커 관리
# 워커는 스레딩함(ThreadPoolExecutor 사용)

from dask.distributed import Client

def square(x):
    return x**2

if __name__ == "__main__":
    client = Client()
    # 설정에따라 다른 컴퓨터에 있는 워커를 사용가능.
    # client를 이용하여, local computer의 병렬코드를 그대로 여러 머신을 사용한 분산처리에 이용가능

    print(client) #<Client: 'tcp://127.0.0.1:#' processes=4 threads=8, memory=8.44 GB>

    fut = client.submit(square,2)
    print(fut) #<Future: pending, key: square-c94e3bc4bf0b4c9a5933f7b43187f6b0>
    print(fut.result()) #4


    futs = client.map(square, [0,1,2,3,4,5,6,7,8,9,10])
    print(futs[0:3])
    # [<Future: pending, key: square-72f30fc48e1c42ee95576d0d3088f8db>, 
    # <Future: pending, key: square-89e339991c492cf890f48a2ecb386f31>, 
    # <Future: finished, type: builtins.int, key: square-c94e3bc4bf0b4c9a5933f7b43187f6b0>]
    # 2에대한 결과는 위로부터 캐시되어있다.
    futs_res = client.gather(futs)
    print(futs_res) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

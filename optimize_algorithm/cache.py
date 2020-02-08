# caching
# 실행속도를 위해 메모리 자원을 약간 쓰자
# 함수 연산결과를 메모리에 저장.
# 이후 같은 호출 시 계산 없이 바로 출력

# = memoization
# 이를 이용하면 dynamic programing이라고 함


# lru(least recently used) cache
from functools import lru_cache

@lru_cache(maxsize=16) #<-계산결과 최대 저장 개수를 설정. 개수가 다 차면 오래된 값부터 대체됨.
def sum2(a,b):
    print("Calculating {} + {}".format(a,b))
    return a+b
print(sum2(1,2))
# Calculating 1 + 2
# 3
print(sum2(1,2))
# 3 #<-계산없이 바로 호출되었다

# lru_cache 관련 메소드
# print(sum2.cache_info()) #CacheInfo(hits=1, misses=1, maxsize=16, currsize=1)
sum2.cache_clear()


# ex1
# Fibonacci
@lru_cache(maxsize=None)
def fibonacci(n): #캐싱하면 O(e^N)보다 낮아진다(선형시간이 됨)
    if n<1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)



# comprehension
# for문보다 빠르고 코드가 읽기 쉬워짐
listcomp = [i*i for i in range(100000)] #list comprehension
generexp = (i*1 for i in range(100000)) #generator expression (NOT tuple comprehension)
dictcomp = {i:i for i in range(100000)}


# map, filter 등 iterator에 특정 함수를 적용하는 함수를 이용해
# 루프를 돌리면 메모리 절약에도 도움이 됨
def map_normal(numbers):
    a = map(lambda n: n*2, numbers)
    b = map(lambda n: n**2, a)
    c = map(lambda n: n**0.33, b)
    return max(c)
# map은 generator를 반환함.
# 일련의 과정마다 numbers의 요소에 대고 통째로 계산해서 각 단계의 리스트를 가지고있는 것보다 메모리를 적게 쓴다.


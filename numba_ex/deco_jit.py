import numba as nb
import numpy as np
from time import time

def non_nb_sum_sq(a):
    result = 0
    N = len(a)
    for i in range(N):
        result += a[i]
    return result

# @nb.jit
# @nb.jit((float64[:],)) #타입객체 튜플 넘기면 < arg 타입을 제한해서, 더 최적화
@nb.jit("float64(float64[:])", nopython=True, cache=True) #string으로 넘기면, return_type([arg1_type, ar2_type,...])
def sum_sq(a):
    result = 0
    N = len(a)
    for i in range(N):
        result += a[i]
    return result

# 타입추론을 잘할수있을수록 -> 명시적으로 타입을 넘길수록 빨라짐
# 표현식 연산이 얼마나 최적화 가능한가에 따라 빨라짐

sum_sq.inspect_types() #타입추론효율 및 최적화정보
# 타입이 py-object로 찍혀나오면 최적화 못했다는 것임. 그냥 그부분은 인터프리터로 돌림 > 느려짐.
# nopython=True < 파이썬 타입 사용 금지 (인터프리터 사용 금지).
# 최적화 못 하고 걍 pyobject로 돌릴수밖에 없을 시 오류 뱉음 <-최적화 체크용으로 역이용 가능

x = np.random.rand(10000)

# sum_sq.specialize
# sum_sq.signiture

# vanila for loop
starttime = time()
for i in range(1000):
    non_nb_sum_sq(x)
print(time()-starttime)

# list comp
starttime = time()
for i in range(1000):
    [i**2 for i in x]
print(time()-starttime)


# numpy vector cal
starttime = time()
for i in range(100000):
    (x**2).sum()
print(time()-starttime)


# using numba, for loop
starttime = time()
for i in range(100000):
    sum_sq(x)
print(time()-starttime)

# (걍 넘파이벡터연산이...더빠른데?)
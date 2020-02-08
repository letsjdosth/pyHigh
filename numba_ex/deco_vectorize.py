from time import time

import numba as nb
import numpy as np

# universal function 
# (ufunc, 인자가 matrix-size가 몇이든, 스칼라든, 돌아가는ㅡ  리턴은 스칼라인 함수.)
# (확장 규칙은 넘파이 브로드캐스팅 규칙을 따름)
# 구현시 쉽게 병렬처리 가능
# ex. np.sum

# 간단히 그냥 데코레이터 @nb.vectorize 붙이자

# @np.vectorize
@nb.vectorize
# @nb.vectorize(target="cpu")
def cantor(a, b):
    return int(0.5*(a+b)*(a+b+1)+b)

print(cantor(np.array([1,2]), 2))

starttime = time()
for i in range(10000):
    cantor(np.array([1,3,2,4,3,5,4,5,5,6,5,5,0,5,4,4,]), 2)
print(time()-starttime)

#이건확실히 np.보다 nb.가 빠름
# 병렬처리는 왜 이득못볼까??


# generalized universal function (gufunc)
# 인자에 배열도 허용하는 ufunc
# ex. np.matmul


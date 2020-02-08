# 빠른 배열 계산이 가능
# 특히 배열 차원이 클 때 이득이 큼. np 쓸거면 배열연산으로 다 바꾸자.

# 더 빠른것이 필요하다면 numexpr 패키지 사용
# numpy 코드 해당 라인을 컴파일해버림. 컴파일하며 최적화함. 자동 병렬처리도 함
# 단, 모든 np 함수를 지원하지는 않고(ex. np slicing 등 미지원. 다른 방식으로 돌려 코딩할 것)
# reduce계열 함수(차원을 줄이며 계산하는)를 최대한 뒤로 밀고, 표현식을 압축적으로 써야 함 (함수형 프로그래밍 원칙과 같은 듯)

import numpy as np
import numexpr as ne

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print(A*B) #<-matrix 연산된다
# [[ 5 12]
#  [21 32]]

print(2*A)
# [[2 4]
#  [6 8]]


# broadcasting
# matrix 연산을 위한 배열 차원이 안맞으면, 앞 배열에 차원을 보고, 뒷 배열 차원을 복제해 조정한다
print(A * np.array([1,2]))
# [[1 4]  #<-에러가 안나고 뭔가 튀어나온다
#  [3 8]]
print(A* np.array([[1,2],[1,2]])) #<-A와 연산을 위한 차원으로 B를 개조 (첫 행을 복제)한 후 계산했다
# [[1 4]
#  [3 8]]

# 복제가 매우 빠르긴 함(python loop가 아닌 더 기계에 가까운 알고리즘 사용)
# 음... 쓰지말자...


# 차원 확장
# (5,2) matrix를 (5,10,2) 차원으로 확장하고싶다면 -> np.newaxis를 집어넣으면 해당 차원은 빈 채로 채워진다.
C = np.random.rand(5,2)
print(C[:, np.newaxis, :])
# [[[0.28225967 0.21349282]]
#  [[0.45953862 0.69419065]]
#  [[0.69675585 0.95577746]]
#  [[0.13554897 0.68551804]]
#  [[0.25803051 0.50952783]]]


# 다른 수학연산
print(np.sqrt(np.array([4,9,16]))) # [2. 3. 4.]

array1 = np.array([0.1, 0.5, 0.8])
over03 = (array1 > 0.3)
print(over03) # [False  True  True]
print(array1[over03]) #[0.5 0.8] #<-over03을 mask로 다시 써서, 0.3보다 큰 array1의 요소를 추출

array2 = np.array([
    [1,2,3],
    [4,5,6]
])
print(array2.sum(axis=0)) # [5 7 9] #shape (3,) array
print(array2.sum(axis=1)) # [ 6 15] #shape (,2) array
print(array2.sum()) # 21

array3 = np.array([[1,2], [3,4], [5,6], [7,8]])
norm_of_3 = np.sqrt((array3**2).sum(axis=1))
print(norm_of_3) # [ 2.23606798  5.          7.81024968 10.63014581]


#numexpr
# ex. 100000차원의 두 점 거리 구하기
r1 = np.random.rand(100000,1)
r2 = np.random.rand(100000,1)
#최대한 한 expr에 우겨넣자. string으로 넘겨야한다. #sum은 reduce류 연산. 때문에 이후 연산은 줄을 바꿔서 해야한다.
diffsq = ne.evaluate("sum((r1-r2)**2)") 
diff = ne.evaluate("sqrt(diffsq)")
print(diff)
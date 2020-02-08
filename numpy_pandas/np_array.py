import numpy as np

# np.array
# numpy의 기본 컬렉션은 np.ndarray
# 모든 요소에 대해 동일타입을 강제하는 배열임
# 처음 리스트에서 ndarray로 변환할 때 타입을 명시적으로 지정해볼 수도 있음

array1 = np.array([0,1,2])
print(array1.dtype) # int32

array2 = np.array([0.0, 0.1, 0.2])
print(array2.dtype) # float64

array3 = np.array([1,2,3], dtype= "int64")
print(array3.dtype) # int64

# 캐스팅
array4 = array1.astype("float32")
print(array4.dtype) # float32


# 다차원 array
# nested sequence 사용해 초기화
array2d_1 = np.array([
    [0,1,2],
    [3,4,5]
])
print(array2d_1)
# [[0 1 2]
#  [3 4 5]]
print(array2d_1.shape) # (2, 3)

# reshape
array2d_2 = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
array2d_2 = array2d_2.reshape(4,4) #차원이 잘 맞아야함
print(array2d_2)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]

# 기본 배열
zero_array = np.zeros((3,3)) #<-tuple로 size를 넘긴다
empty_array = np.empty((3,3))
ones_array = np.ones((3,3), dtype="float32")
print(zero_array)
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]
print(empty_array) #<-대충 쓰레기값으로 채워진다.
# [[0.00000000e+000 0.00000000e+000 0.00000000e+000]
#  [0.00000000e+000 0.00000000e+000 2.96439388e-321]
#  [1.09494983e-311 1.09494983e-311 0.00000000e+000]]
print(ones_array)
# [[1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]

# 특정 배열 객체와 차원을 맞추는 기본 배열
np.zeros_like(array2d_2)
np.empty_like(array2d_2)
np.ones_like(array2d_2)

# uniform(0,1) 랜덤 배열
random_array = np.random.rand(3,3) #<-여긴 size를 tuple로 안 받고...
print(random_array)
# [[0.73352089 0.05094131 0.81506821]
#  [0.59314847 0.61138191 0.01132189]
#  [0.03375204 0.32520585 0.22873401]]


# 접근 : R과 매우 비슷 (비워놓지말고 :를 채우자)
array2d_3 = np.array([
    [0,1,2],
    [3,4,5],
    [6,7,8]
])
print(array2d_3[0]) #[0,1,2]
print(array2d_3[0,0]) #0
print(array2d_3[0,:]) #[0,1,2]
print(array2d_3[:,0]) #[0,3,6]

# 슬라이싱 (start:end:step. end는 해당인덱스 포함안함)
# 주의: np array의 슬라이스는 메모리뷰임. 
# 즉 잘린 객체를 새로 만드는것이 아니라 원래 객체 자체를 똑같이 보고 출력만 내는 것임
# 따라서 슬라이스한 채로 수정하면, 원래 객체도 수정되어버림.
# (덕분에 빠르긴 한데...)
print(array2d_3[0:2])
# [[0 1 2]
#  [3 4 5]]
print(array2d_3[0:2, 0:2])
# [[0 1]
#  [3 4]]
print(array2d_3[0:2, :])
# [[0 1 2]
#  [3 4 5]]
print(array2d_3[:, 0:2])
# [[0 1]
#  [3 4]
#  [6 7]]

view_test_array = np.array([1,1,1,1])
test_view = view_test_array[0:2]
test_view[0] = 2
print(view_test_array) #[2 1 1 1] #<- ㅡㅡ...

# fancy indexing
# 접근시 [] 안에 다시 np.array 혹은 일반 파이썬 리스트를 집어넣어(tuple은 안됨. tuple unpacking되어 각 인덱스 취급당함)
# 해당 인덱스 값을 묶은 array를 다시 얻을 수 있음
array3 = np.array([9,8,7,6,5,4,3,2,1,0])
idx = [0,2,3]
print(array3[idx]) #[9 7 6]
print(array3[[0,2,3]]) #[9 7 6]

array2d_4 = np.array([
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [9,10,11]
])
idx1 = np.array([2,3])
idx2 = [0,1]
print(array2d_4[idx1, idx2]) #[ 6 10] #<- (2,0)과 (3,1) 두 요소가 꺼내진 후 묶인다
print(array2d_4[np.array([1,3]), 1:3]) #슬라이싱과 fancy indexing 합쳐서 사용가능. #<-1,3행(0부터 셈에 주의), 1~2열(0부터 세고, 맨 뒤는 포함 안함에 주의)
# [[ 4  5]
#  [10 11]]

# bool mask
# true자리만 추출해버림
array4 = np.array([0,1,2,3,4,5])
npmask = np.array([True, False, True, True, False, False])
mask = [True, False, True, True, False, False]
print(array4[npmask]) #[0 2 3]
print(array4[mask]) #[0 2 3]


# 더 빠른 접근을 위해, 하위 함수인 
# np.take(array, idx_list, axis)
# np.compress(array, bool_list, axis)
# 를 사용해볼 수 있음



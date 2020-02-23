# * 와 &

cdef double a
from libc.stdio cimport printf
printf("%p", &a) # & : 메모리 주소 연산자

cdef double *a_pointer
a_pointer = &a # * : 메모리 주소 변수 선언

a = 3.0
# printf(*a_pointer)
# *: 역참조 연산자


# 배열 선언
cdef double arr1[10] #10*1 배열
cdef double arr2[5][2] #5*2 배열 
# 인덱싱
arr1[0] = 1.0
# (슬라이싱이나, 스마트 인덱싱은 지원 안 함)

printf("%pn", arr1)
printf("%pn", &arr1[0])


#numpy 배열 선언
cimport numpy as c_np
c_np.ndarray[double, ndim=2] np_arr 
#[]는 버퍼 문법이라고 함. 2차원 double 배열 생성
# 그냥 python의 np 배열보다 cython 것이 loop를 약 50배 바르게 돈다고 함



# 메모리뷰
# 타 메모리 부분에 대한 뷰. 메모리뷰를 통해 메모리 내용을 읽거나 수정하는 것이 가능
cdef int[:] mv1dim
cdef double[:,:] mv2dim

import numpy as np
arr_np = np.zeros(10, dtype='int32')
cdef int[:] mv_arr_np
mv_arr_np = arr_np #객체에 메모리뷰 바인딩
mv_arr_np[2] = 1 #인덱싱/수정
print(arr_np) 
# 메모리뷰는 기타 np 슬라이싱 문법도 지원
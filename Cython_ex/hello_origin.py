
def hello():
    print("Hello, World!")

# 수동 컴파일 시도
# cython -3 -D MS_WIN64 hello.py
# gcc -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing -DMS_WIN64 -I "C:/Users/rtoru/AppData/Local/Programs/Python/Python37/include" -o hello.so hello.c

# 에러남
# https://github.com/cython/cython/issues/2670
# https://github.com/cython/cython/issues/2670#issuecomment-432212671

# hello.c:201:41: warning: division by zero [-Wdiv-by-zero]
#      enum { __pyx_check_sizeof_voidp = 1 / (int)(SIZEOF_VOID_P == sizeof(void*)) };
#                                          ^
# hello.c:201:12: error: enumerator value for '__pyx_check_sizeof_voidp' is not an integer constant
#      enum { __pyx_check_sizeof_voidp = 1 / (int)(SIZEOF_VOID_P == sizeof(void*)) };
#             ^~~~~~~~~~~~~~~~~~~~~~~~

# gcc 가 win64에서 python 관련을 지원안한다고함
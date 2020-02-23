cdef inline int max(int a, int b):
    return a if a>b else b

cdef inline int min(int a, int b):
    return a if b>a else b
# cytnon compiler에 hint를 주자

# 변수 type hint
cdef int i
cdef double a,b = 2.0, c=3.0

cdef int c = 0
cdef double d = <double> c #casting

# C 기본타입 모두 가능 (struct까지)

# 단, 그 외의 파이썬 객체는 object로 선언해야함
# 단 object는 Cython이 최적화를 잘 못하므로, 성능이득이 별로 없음


# 함수 type hint
# def: 타입검사하는 파이썬 임포트가능 버전
def max_python(int a, int b):
    return a if a>b else b

# cdef: cython 전용 버전. 잘 최적화됨
cdef int max_cython(int a, int b):
    return a if a>b else b

# cpdef: cython 전용 버전과 python 임포트가능 버전을 동시 생성
cpdef int max_hybrid(int a, int b): 
    return a if a>b else b

# inline: 컴파일시 인라인화. C에서의 호출부담을 줄임. 짧은함수에서 유용
cdef inline int max_cython_inline(int a, int b):
    return a if a>b else b


# class hint
# class member중 property는 C struct로 구현되어 C에서 곧바로 접근함->빠름
# method는...(?)
# 주의: 멤버는 cython 같은 파일 안에서는 모두 public지만
# 컴파일 후 python에 이 클래스 임포트해서는 접근이 안됨.
# 컴파일 후 바깥 py 파일에서, cython class 멤버에 직접 접근이 필요하다면 모두 public으로 선언할 것
cdef class Point:
    cdef double x
    cdef double y
    cdef public int point_id

    def __init__(self, double x, double y):
        self.x = x
        self.y = y

cdef double norm(Point p):
    return (p.x**2 + p.y**2)**0.5
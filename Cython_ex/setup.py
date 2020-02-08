from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='Hello',
    ext_modules = cythonize('hello.py')
)

# mingw gcc가 python3 64bit을 지원 안한다고함
# 때문에 distutils도 gcc를 지원 안 함
# distutil로 하려면, ms가만든 msvc 써야함
# 음..설치하자...


# python setup.py build_ext --inplace
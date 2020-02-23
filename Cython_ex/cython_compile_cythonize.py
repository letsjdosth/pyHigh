from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='assignmentArray',
    ext_modules = cythonize('assignment_array.pyx')
)

# mingw gcc가 python3 64bit을 지원 안한다고함
# 때문에 distutils도 gcc를 지원 안 함
# distutil로 하려면, ms가만든 msvc 써야함
# 음..설치하자...


# python cython_compile_cythonize.py build_ext --inplace
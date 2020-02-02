# cProfile
# c로 작성된 프로파일러. 가벼움. (표준라이브러리의 그냥 profile은 파이썬으로 작성되었고 무거움.)

# 사용: 1. 명령행 2. 파이썬 스크립트
# 1. python cProfile -s tottime -o prof.out simul.py
# 2.
from simul import benchmark
import cProfile

cProfile.run("benchmark()")

# 혹은 다음과 같이 
# pr = cProfile.Profile()
# pr.enable()
# benchmark()
# pr.disable()
# pr.print_stats()

# 출력:: 
# 7007 function calls in 0.691 seconds

#    Ordered by: standard name

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.691    0.691 <string>:1(<module>)
#      3000    0.001    0.000    0.001    0.000 random.py:372(uniform)
#         1    0.000    0.000    0.000    0.000 simul.py:13(__init__)
#         1    0.690    0.690    0.690    0.690 simul.py:16(evolve)
#      1000    0.000    0.000    0.000    0.000 simul.py:7(__init__)
#         1    0.000    0.000    0.691    0.691 simul.py:88(benchmark)
#         1    0.001    0.001    0.001    0.001 simul.py:89(<listcomp>)
#         1    0.000    0.000    0.691    0.691 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      3000    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}

# ncalls: 호출횟수
# tottime: 타함수호출제외 함수본체 실행시간
# percall: 이 함수 1회호출시 소모시간
# cumtime: 이 함수 호출로 보낸 총시간
# filename:lineno: 파일명 행번호

# 하위호출제외 함수본체 소모 시간인 tottime<이 중요


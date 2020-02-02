# timeit module
# 1. (timeit 직접 import하지말고 콘솔에서) python -m timeit -s 'from simul import benchmark' 'benchmark()'
# 2. 스크립트에 timeit import후 다음 실행
import timeit
result = timeit.repeat('benchmark()',
                        setup = 'from simul import benchmark',
                        number = 10,
                        repeat = 3)
print(result)
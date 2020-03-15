# dask.array
# Dask Array implements a subset of the NumPy ndarray interface using blocked algorithms, 
# cutting up the large array into many small arrays. 
# This lets us compute on arrays larger than memory using all of our cores.

# numpy array에 의존

import numpy as np
import dask.array as da

a = np.random.rand(30)
a_da = da.from_array(a, chunks=10) #10개 단위로 쪼갠다. (아래 참고) 이것이 병렬 단위가 된다.

print(a_da) 
#dask.array<array, shape=(30,), dtype=float64, chunksize=(10,), chunktype=numpy.ndarray>

print(dict(a_da.dask))
# {('array-c71bc9043391197db52d7b1980861a99', 0): 
# (<built-in function getitem>, 'array-original-c71bc9043391197db52d7b1980861a99', (slice(0, 10, None),)),
# 
#  ('array-c71bc9043391197db52d7b1980861a99', 1): 
# (<built-in function getitem>, 'array-original-c71bc9043391197db52d7b1980861a99', (slice(10, 20, None),)),
# 
#  ('array-c71bc9043391197db52d7b1980861a99', 2): 
# (<built-in function getitem>, 'array-original-c71bc9043391197db52d7b1980861a99', (slice(20, 30, None),)), 
# 
# 'array-original-c71bc9043391197db52d7b1980861a99': 
# array([0.67752356, 0.93736136, 0.38408372, 0.3905681 , 0.55233118,
#        0.89892823, 0.24806201, 0.67185382, 0.15809548, 0.32569257,
#        0.69492944, 0.15358525, 0.97147786, 0.42040474, 0.54160583,
#        0.08067313, 0.08397948, 0.0064042 , 0.98605042, 0.20345672,
#        0.99345078, 0.12486862, 0.2986112 , 0.27293128, 0.61420433,
#        0.8426881 , 0.5783514 , 0.44915112, 0.21403005, 0.43007314])}



# ex: monte carlo pi val estimate
N = 100000
chunksize = 20000

x_data = np.random.uniform(-1, 1, N)
y_data = np.random.uniform(-1, 1, N)

x = da.from_array(x_data, chunks=chunksize)
y = da.from_array(y_data, chunks=chunksize)
print(x.shape)

hit_test = x**2 + y**2 <= 1
hits = hit_test.sum()
pi = 4 * hits / N

# pi.visualize() #need: graphviz package
print(pi.compute()) #3.14056
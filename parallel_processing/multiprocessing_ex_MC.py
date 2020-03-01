# monte carlo approx
# for pi value

import random
import multiprocessing

samples = 1000000
hits = 0

n_tasks = 10
chunk_size = int(samples / n_tasks)

def sample():
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)

    if x**2 + y**2 <= 1:
        return 1
    else:
        return 0

def sample_multiple(samples_partial):
    return sum(sample() for i in range(samples_partial))

if __name__ == "__main__":
    with multiprocessing.Pool() as p:
        result_async = [p.apply_async(sample_multiple, (chunk_size,)) for i in range(n_tasks)]
        hits = sum(r.get() for r in result_async)
    
    pi = 4.0 * hits / samples
    print(pi)
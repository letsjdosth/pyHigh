# Pool 사용
# https://docs.python.org/ko/3/library/multiprocessing.html?highlight=pool#module-multiprocessing.pool

import multiprocessing

def square(x):
    return x*x

if __name__ == "__main__":
    inputs = [0,1,2,3]
    with multiprocessing.Pool(4) as p:
        outputs = p.map(square, inputs)
        print(outputs)
    
    with multiprocessing.Pool(4) as p:
        outputs_async = p.map_async(square, inputs)
        outputs_result = outputs_async.get()
        print(outputs_result)

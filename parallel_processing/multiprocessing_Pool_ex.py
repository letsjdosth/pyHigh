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
        outputs_async = p.map_async(square, inputs) #iterable을 넘긴다. 하나짜리 arg(여러개면 starmap)
        outputs_result = outputs_async.get()
        print(outputs_result)

    with multiprocessing.Pool(4) as p:
        output_apply_async = [p.apply_async(square, (i,)) for i in range(100)] #걍 하나씩 등록한다. arg는 iterable로 넘겨야함
        outputs_apply_result = [r.get() for r in output_apply_async]
        print(outputs_apply_result)

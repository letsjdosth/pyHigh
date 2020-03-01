# Executor interface
# https://docs.python.org/ko/3/library/concurrent.futures.html?concurrent.futures.ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor, wait, as_completed

def square(x):
    return x*x

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers= 4) as executor:
        fut2 = executor.submit(square, 2) #future 반환
        fut3 = executor.submit(square, 3)
        print(fut2) #<Future at 0x223e76df630 state=running>
        wait([fut2, fut3])
        fut_results = as_completed([fut2,fut3]) 
        print(fut_results) #<generator object as_completed at 0x0000022B1C24CC00>
        print([fut.result() for fut in fut_results]) #[4, 9] #<-순서 바뀔 때 있음

    with ProcessPoolExecutor(max_workers= 4) as executor:
        map_ex = executor.map(square, [0,1,2,3,4,5])
        print(map_ex) #<generator object _chain_from_iterable_of_lists at 0x000001D916DECC00>
        print(list(map_ex)) #[0, 1, 4, 9, 16, 25]
# 제너레이터를 이용한 코루틴
# 참고 제너레이터 기반 코루틴에 대한 지원은 폐지되었고 파이썬 3.10에서 삭제될 예정입니다.
# https://docs.python.org/ko/3/library/asyncio-task.html#generator-based-coroutines

def range_generator(n):
    i = 0
    while(i<n):
        print("generating value {}".format(i))
        yield i
        i += 1

generator = range_generator(3)
next(generator)
next(generator)
next(generator)
# generating value 0
# generating value 1
# generating value 2

# next(generator) #StopIteration

def parrot():
    while True:
        message = yield
        print("Parrot says : {}".format(message))

parrot_gen = parrot()
parrot_gen.send(None)
parrot_gen.send("Hello")
parrot_gen.send("World")
# Parrot says : Hello
# Parrot says : World


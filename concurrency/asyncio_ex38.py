import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    # 동시실행 예약 : task
    task1 = asyncio.create_task(
        say_after(1, 'Hi')
    )
    task2 = asyncio.create_task(
        say_after(2, 'python!')
    )
    
    await task1
    await task2
    # await say_after(3, 'hello, world!') #비동기적으로 동시에 실행할것이라면 task에 넣자


    print(f"finished at {time.strftime('%X')}")



asyncio.run(main())
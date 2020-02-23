import asyncio

# 기본 루프
loop = asyncio.get_event_loop()
#3.8에서는 이거 말고 asyncio.run() 사용

def callback():
    print("Hello, asyncio")
    loop.stop()

loop.call_later(1.0, callback)
loop.run_forever()
import asyncio

@asyncio.coroutine
def func1():
    while True:
        print("func1")
        yield from asyncio.sleep(1)

@asyncio.coroutine
def func2():
    while True:
        print("func2")
        yield from asyncio.sleep(1)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    tasks = asyncio.wait([func1(), func2()])
    loop.run_until_complete(tasks)

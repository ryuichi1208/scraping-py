import time
import concurrent.futures

def function1():
    while True:
        print("function1")
        time.sleep(1)

def function2():
    while True:
        print("function1")
        time.sleep(1)

def function2():
    while True:
        print("function2")
        time.sleep(1)


if __name__ == "__main__":
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
    executor.submit(function1)
    executor.submit(function2)


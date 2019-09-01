import time
import threading

def func1():
    while True:
        print("func1")
        time.sleep(1)

def func2():
    while True:
        print("func2")
        time.sleep(1)

if __name__ == "__main__":
    thread_1 = threading.Thread(target=func1)
    thread_2 = threading.Thread(target=func2)

    thread_1.start()
    thread_2.start()

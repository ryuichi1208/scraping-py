import sys, os
import inspect

class z:
    def deco(func):
        def wrapper(*args, **kwargs):
            print("aaa")
            func()
            print("bbb")
        return wrapper


@z.deco
def start():
    print("start")

def end():
    print("end")

start()
obj = -1
for x in dir(obj):
  print(x)


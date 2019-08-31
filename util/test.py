def add(x, y):
    return x+y

def handler(func, *args):
    print(args)
    return func(args)

print(handler(add, (3, 4)))

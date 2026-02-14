def logger(func):
    def wrapper(*args, **kwargs):
        print("Calling", func.__name__)
        return func(*args, **kwargs)
    return wrapper

@logger
def greet(name):
    print("Hello,", name)

greet("Alice")

def add(a: int, b: int) -> int:
    return a + b

from contextlib import contextmanager

@contextmanager
def my_resource():
    print("Acquired")
    yield
    print("Released")

with my_resource():
    print("Inside block")

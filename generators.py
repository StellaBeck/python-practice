def even_numbers(n):
    i = 1
    while i <= n:
        if i%2 == 0:
            yield i
        i += 1

def fibonacci(n):
    a, b = 1, 1
    i = 0
    while i < n:
        yield a
        a, b = b, a + b
        i += 1

def forever():
    list = ['A', 'B', 'C']
    i = 0
    while True:
        yield list[i]
        i += 1
        if i >= len(list):
            i = 0

def square_numbers(n):
    i = 1
    while i*i <= n:
        yield i * i
        i += 1

gen = square_numbers(100)
print(next(gen))
print(next(gen))
print(next(gen))
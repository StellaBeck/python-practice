add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y

l = ["Tom", "Alice", "Bob"]
print(sorted(l, key= lambda x: x[-1]))
print(list(filter(lambda x: len(x) <= 3, l)))

def my_map(func, lst):
    return [func(x) for x in lst]

def make_power(n):
    return lambda x: x ** n
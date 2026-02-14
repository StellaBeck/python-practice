def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)

print_info(name="Alice", age=25)
x = 10  # global

def modify():
    global x
    x = 20  # modifies global x

modify()
print(x)  # 20

def demo(a, *args, **kwargs):
    print("a =", a)
    print("args =", args)
    print("kwargs =", kwargs)

demo(1, 2, 3, x=10, y=20)
# a = 1
# args = (2, 3)
# kwargs = {'x': 10, 'y': 20}

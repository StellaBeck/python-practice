class Person:
    def __init__(self, name, age):  # constructor
        self.name = name
        self.age = age

    def greet(self):                # instance method
        return f"Hi, I’m {self.name}, {self.age} years old."

p = Person("Alice", 30)
print(p.greet())  # Hi, I’m Alice, 30 years old.

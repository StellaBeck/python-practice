def say_hello():
    print("Hello")

def sum(a, b):
    return a+b

def dif(a, b):
    return a-b

def mul(a, b):
    return a*b

def quo(a, b):
    return a//b

def is_even(n):
    if n%2:
        return False
    else:
        return True

def greet_user(name, language="English"):
    if(language == "Spainish"):
        print(f"Hola, {name}")
    elif(language == "French"):
        print(f"Bonjour, {name}")
    else:
        print(f"Hello, {name}")

def factorial(n):
    fact = 1
    while(n>0):
        fact = fact*n
        n -= 1

    return fact

def welcome(name):
    print(f"Welcome, {name}")

def area(length, width):
    return length*width

def max_of_three(a, b, c):
    if a > b:
        if a > c:
            return a
    else:
        if b > c:
            return b
    return c

def simple_interest(p, r, t):
    return (p*r*t)/100

def power(base, exponent):
    n = 1
    for i in range(exponent):
        n *= base
    return n

def reverse_string(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev

def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count

def is_palindrome(s):
    i = s.__len__()-1
    for ch0 in s:
        if ch0 != s[i]:
            return False
        if i < s.__len__()//2:
            break
        i -= 1

    return True

def fibonacci(n):
    list = [1, 1]
    for i in range(n-2):
        list.append(list[i]+list[i+1])
    return list

def digit_sum(n):
    sum = 0
    while n > 0:
        sum += n%10
        n = n//10
    return sum

print(is_even(5))
print(factorial(4))
print(max_of_three(2, 3, 1))
print(power(2, 5))
print(reverse_string("Hello, Anne"))
print(count_vowels("Hello, Anne"))
print(is_palindrome("huioooiuh"))
print(fibonacci(12))
print(digit_sum(23432))
t = ()
"""
for i in range(5):
    t = t + (int(input("Enter a number: ")),)

smallest = 0
for i in range(len(t)-1):
    if(t[i] < t[i+1]):
        smallest = t[i]
print(t)
print("Smallest number is:", smallest)
"""
data = ("Python", 3.11, "stable")
name, version, status = data
print(f"Name: {name}, Version: {version}, Status: {status}")

def swap(a, b):
    return b, a

print(swap(5, 10))
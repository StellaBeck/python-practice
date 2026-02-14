s0 = set()

for i in range(5):
    s0.add(int(input("Enter a number: ")))

print(s0)

s1 = {52, 3, 5, 2, 7}
union = s0 | s1
print("Union of sets is:", union)
print("Intersection of sets is:", s0 & s1)
print("difference of sets is:", s0 - s1)
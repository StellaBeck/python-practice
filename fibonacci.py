terms = int(input("Enter number of terms: "))
a, b = 0, 1
sequence = []
for _ in range(max(terms, 0)):
    sequence.append(a)
    a, b = b, a + b
print("Fibonacci:", sequence)

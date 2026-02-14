nums = [2, 4, 0, 3]
nums.append(1)
nums.remove(2)
nums.sort()
print(nums)
"""
l = []
for i in range(5):
    l.append(int(input("Enter a number: ")))
print(l)
sum = 0
for i in l:
    sum += i
print(sum/5)
"""
l0 = [x*x for x in range(10) if x % 2 == 0]
words = ["hello", "world", "hello", "python"]
l1 = [word[0] for word in words]
l2 = [word.upper() for word in words]
l3 = [word for word in words if len(word) > 4]
matrix = [[1, 2], [3, 4], [5, 6]]
l4 = [j for row in matrix for j in row]
print(l4)
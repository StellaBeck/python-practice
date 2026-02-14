sentence = input("Enter a sentence: ")
words = sentence.split()

d = {}
for i in words:
    if (i in d.keys()):
        d[i] += 1
    else:
        d[i] = 1

print(d)
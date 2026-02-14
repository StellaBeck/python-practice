grades = {
    "Yvonne": 'A',
    "Lynn": 'B',
    "Stella": 'C'
}

print(grades)
name = input("Enter a name\n")
if (name in grades.keys()):
    print("Grade: ", grades[name])
else:
    print("Name not found.")

info = {"a": 1, "b": 2}
for key, value in info.items():
    print(f"key: {key}, value: {value}")
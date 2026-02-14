import json

# From file
with open("data.json", "r") as f:
    data1 = json.load(f)

# From string
text = '{"name": "Alice", "age": 25}'
data2 = json.loads(text)

print(data1, data2)

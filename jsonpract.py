import json

dictionary = {"name": "Stella", "hobby": "coding", "country": "Myanmar"}
with open("data.json", "a") as file:
    json.dump(dictionary, file, indent=4)

with open("data.json", "r") as file:
    data = json.load(file)
    print(data)
with open("name.txt", 'w') as file:
    file.write(input("Enter a name.\n"))
with open("name.txt", 'r') as file:
    name = file.read().strip()
    print("Hello,", name)
    with open("story.txt", 'r') as story_file:
        story = story_file.read()
        if (name in story):
            print("Your name is in the story!")
with open("note.txt", 'r') as file:
    #lines = file.readlines()
    #countLines = len(lines)
    with open("backup.txt", 'w') as backup:
        backup.write(file.read())
with open("friends.csv", 'r') as file:
    friends = file.readlines()
    for friend in friends:
        name, age = friend.strip().split(',')
        print(f"{name} is {age} years old.")
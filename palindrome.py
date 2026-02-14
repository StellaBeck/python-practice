text = input("Enter text: ")
cleaned = "".join(text.lower().split())
if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

num = int(input("Guess a number from 0 to 9: "))
while num != 7:
    if num > 8:
        print("Too high! Guess again.")
    elif num < 6:
        print("Too low! Guess again.")
    else:
        print("Wrong! Guess again.")
    num = int(input())
print("Correct!")
def main():
    #import cs50
    #from cs50 import get_int, get_float

    name = input("What's your name?")
    print(f"Fuck you, {name.upper()}")
    #age = cs50.get_int("age: ")
    age = int(input("age: "))

    if age < 18:
        print("You're underaged!")
    elif age == 18:
        print("Good!")
    else:
        print("You are an adult!")

    print(f"{(age/2):.4f}")
    for i in range(3):
        print("meow!")

    IsSingle()

def get_int(prompt):
    while True:
        try:
            return(int(input(prompt)))
        except ValueError:
            pass
    
def IsSingle():
    single = input("Are you single?").lower()

    if single == "yes" or single == 'y':
        print("Good!")
    elif single in ["n", "no"]:
        print("OK!")

main()
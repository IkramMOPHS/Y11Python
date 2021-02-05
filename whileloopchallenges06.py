endloop = "n"

num = int(input("Enter a number: "))

while endloop == "n":

    if num < 10:
        print("Too low, guess again")
        num = int(input("Enter a number: "))

    elif num > 20:
        print("Too high, guess again")
        num = int(input("Enter a number: "))

    else:
        endloop = "y"

print("Thank you")

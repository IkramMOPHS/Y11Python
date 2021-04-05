#whileloopchallenges05

compnum = 50
newguess = "y"
guess = int(input("Enter a number: "))

count = 1

while newguess == "y":

    if guess != compnum:
        print("Incorrect guess")

        if guess > compnum:
            print("Too high")

        else:
            print("Too low")

        newguess = str(input("Do you want another guess? y/n: ")).lower()
        if newguess == "y":
            guess = int(input("Enter a number: "))
            count = count + 1

    else:
        print("You got it!")
        newguess = "n"

print("It took you" ,count, "times to guess the value.")

#whileloopchallenges04

ctrl = "y"

count = 0

while ctrl == "y":

    name = str(input("Enter a name for the party: "))
    print(name, "has been invited.")

    count = count + 1

    ctrl = str(input("Do you want to invite anyone else? y/n: ")).lower()



print(count, "people have been invited to the party.")


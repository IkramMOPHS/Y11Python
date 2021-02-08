invite = int(input("Enter the number of people you want to invite to a party: "))

if invite < 10:

    for x in range(0, invite):
        name = str(input("Enter a name to invite to the party: "))
        print("")
        print(name, "has been invited to the party.")
        print("")

else:
    print("Too many people")

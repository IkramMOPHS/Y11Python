#.find()stringchallenges05

number = str(input("Enter a phone number: "))
target = "0"

if number.find(target) == 0:
    print("Valid UK number")

else:
    print("Not a valid number")

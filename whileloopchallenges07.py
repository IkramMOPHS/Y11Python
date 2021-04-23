#Ikram Munye 
#whileloopchallenges07

value = 10

while value != 0:

    print("There are" ,value, "green bottles hanging on the wall.")
    print(value, "green bottles hanging on the wall")
    print("And if one green bottle should accidentally fall...")

    print("")

    guess = int(input("How many green bottles will be hanging on the wall? "))

    if guess == value - 1:
        print("")
        print("There will be" ,value, "green bottles hanging on the wall.")
        value = value - 1
        value = guess

    else:
        print("")
        print("Try again")
        value = int(input("How many green bottles will be hanging on the wall? "))

print("")
print("There will be no green bottles hanging on the wall")

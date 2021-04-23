#Ikram Munye 
#.find()stringchallenges06

loop = "y"

while loop == "y":

    number = str(input("Enter a number: "))
    length = (len(number))
    target = "0"

    valid = 0
    nonvalid = 0

    if length == 11 and number.find(target) == 0:
        print("Valid UK number.")

        print("")

        valid = valid + 1

    else:
        print("Not a UK mobile phone number.")

        print("")

        
        nonvalid = nonvalid + 1

    loop =  str(input("Do you want to check another number? y/n: ")).lower()
    print("")


print("Finished")
print("")
print(nonvalid, "non-valid UK numbers")
print("")
print(valid, "valid UK numbers.")

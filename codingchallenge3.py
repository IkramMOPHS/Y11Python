print("Leauge Registration")

print("")

firstname = str(input("Enter your first name: "))
print("")
lastname  = str(input("Enter your last name: "))
print("")
nickname = str(input("Enter your nickname: "))
print("")
skill_level = chr(input("What is your skill level? E for Expert or C for Casual: ")).upper()
print("")
email = str(input("Enter your email address: "))
print("")
print("")

print("First Name:", firstname)
print("Last Name:", lastname)
print("Nickname:", nickname)
print("Email:", email)

correct = str(input("Are these details correct? Y or N: ")).upper()

while correct == "Y":

    namechange = str(input("Do you want to change your name? Y or N: ")).upper()

    if namechange == "Y":
        newname = str(input("Enter your first name: "))
        print(newname)

    else:
        print(firstname)


    lastnamechange = str(input"Do you want to change your lastname? Y or N: ")).upper()

    if lastnamechange == "Y":
        newlastname = str(input("Enter your last name: "))
        print(newlastname)

    else:
        print(lastname)

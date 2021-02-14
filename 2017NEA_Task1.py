title = "League Registration"

print(title)

print("")

name = str(input("Enter your name: ")).title()

print("")

lastname = str(input("Enter your last name: ")).title()

print("")

nickname= str(input("Enter your nickname: "))

print("")

email = str(input("Enter your email address: "))

print("")

print("Enter your skill level")
skill = str(input("E for Expert and C for Casual: ")).upper()

if skill == "E":
    print("")
    print("Expert selected")

elif skill == "C":
    print("")
    print("Casual selected")

else:
    print("Select a correct gamemode")
    print("")
    skill = str(input("E for Expert and C for Casual: ")).upper()

print(name)
print("")
print(lastname)
print("")
print(nickname)
print("")
print(email)
print("")
print(skill)

print("")

correct = str(input("Are these details correct? y/n: ")).lower()

while correct == "n":
    name = str(input("Enter your name: "))

    print("")
    
    lastname = str(input("Enter your last name: "))

    print("")

    nickname= str(input("Enter your nickname: "))

    print("")

    email = str(input("Enter your email address: "))

    print("")

    print("Enter your skill level")

    print("")

    skill = str(input("E for Expert and C for Casual: ")).upper()

    if skill == "E":
        print("")
        print("Expert selected")

    elif skill == "C":
        print("")
        print("Casual selected")

    else:
        print("Select a correct gamemode")
        print("")
        skill = str(input("E for Expert and C for Casual: ")).upper()

    print(name)
    print("")
    print(lastname)
    print("")
    print(nickname)
    print("")
    print(email)
    print("")
    print(skill)
    print("")

    correct = str(input("Are these details correct? y/n: ")).lower()

else:
    print("")

print(title)

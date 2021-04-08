#2017NEA_Task1

title = "League Registration"                   #saves the title in a variable so recall is easier at the end

print(title)

print("")

name = str(input("Enter your name: ")).title()      #asks user to enter their name

print("")                                           #creates gaps so the user does not misread or struggle

lastname = str(input("Enter your last name: ")).title()     #.title() makes it so the name automatically makes the first letter capital while the res are lowercase

print("")

nickname= str(input("Enter your nickname: "))

print("")

email = str(input("Enter your email address: "))

print("")

print("Enter your skill level")
skill = str(input("E for Expert and C for Casual: ")).upper()   #.upper() makes it so the letter inputted turns into an uppercase

if skill == "E":                                                #if statment: if the condition of E is met, then a certain output is displayed, same with C
    print("")
    print("Expert selected")

elif skill == "C":
    print("")
    print("Casual selected")

else:
    print("Select a correct gamemode")              #ensures the person has selected a correct gamemode
    print("")
    skill = str(input("E for Expert and C for Casual: ")).upper()

print(name)                                                         #line 39 - 47 prints the details so the user can see if there are any mistakes
print("")
print(lastname)
print("")
print(nickname)
print("")
print(email)
print("")
print(skill)

print("")

correct = str(input("Are these details correct? y/n: ")).lower()                #and if there are mistakes, the user can re-enter all their details once again 

while correct == "n":                                                           #the while loop repeats until the user enters all the correct details, which they answer with y/n on line 100
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

    correct = str(input("Are these details correct? y/n: ")).lower()        #allows the user to re-enter details if incorrect

else:
    print("")

print(title)            #returns the user to the title screen

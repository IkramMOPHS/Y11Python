print("Welcome new player")
print("To register, you need to input your age, email address and player name.")

print("")
print("")
print("")
print("")
print("")



email = str(input("Please enter your email: "))
age = int(input("Please enter your age: "))
playername = str(input("Please enter your player name: "))

print("")
print("")
print("")
print("")
print("")
print("")
print("")

emailchange = str(input("Would you like to change your email? Enter Y or N. "))

if emailchange == "Y":
  email = str(input("Please enter your new email: "))
  print("")
  print("")
  print("")
  print("")
  print("")

    
else:
  print("Your email is",email)

  print("")
  print("")
  print("")
  print("")



namechange = str(input("Would you like to change your name? Enter Y or N. "))

print("")
print("")
print("")
print("")
print("")
print("")
print("")


if namechange == "Y":
    playername = str(input("Please enter your player name: "))

else:
    print("Your player name is",playername)

print("")
print("")
print("")
print("")
print("")
print("")
print("")
    

agechange = str(input("Would you like to change your age? Enter Y or N. "))

if agechange == "Y":
    age = int(input("Enter your age: "))

else:
    print("Your age is",age)



print("Your name is",playername)
print("Your age is",age)
print("And your email address is",email)
print("Welcome,",playername)

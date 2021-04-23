#Ikram Munye 
#forloopschallenges07

total = 0

for i in range(0,5):

    number = int(input("Please enter a number: "))

    add = "yes"

    decision = str(input("DO you want the number to be added to the total? Yes or No: ")).lower()

    if decision == add:
        total = total + number

    else:
        print("It will not be included")

print(total)

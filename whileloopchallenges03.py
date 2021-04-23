#Ikram Munye 
#whileloopchallenges03

firstnum = int(input("Enter a number: "))

total = firstnum

letter = "y"

while letter == "y":

    newnum = int(input("Enter a number: "))

    total = total + newnum

    letter = str(input("Do you want to add a new number? y/n: ")).lower()


print(total)

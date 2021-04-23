#Ikram Munye 
#forloopschallenges08

direction = str(input("Which direction do you want to go? u/d: ")).lower()

if direction == "u":
    num = int(input("Enter a top number: "))

    for i in range(0,num):
        print(1+i)

elif direction == "d":
    num = int(input("Enter a bottom number less than 20: "))

    for i in range(0, 21-num):
        print(20-i)

else:
    print("I don't understand")

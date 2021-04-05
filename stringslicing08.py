#stringslicing08

loop = 0

loopcounter = "y"

while loopcounter == "y":
    lastname = str(input("Enter your last name: ")).title()

    loop = loop + 1

    loop = str(loop)

    print(lastname[0:3] + loop)

    loopcounter = str(input("Any more membership numbers? y/n: ")).lower()

    loop = int(loop)
   

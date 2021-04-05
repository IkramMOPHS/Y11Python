#stringslicing07

name = str(input("Enter your first name: ")).title()

if name[0] == "A" or name[0] == "E" or name[0] == "I" or name[0] == "O" or name[0] == "U":

    name = " "
    print(name)

else:
    print(name)

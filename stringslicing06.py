name = str(input("Enter your first name: ")).lower()
length = len(name)

if length < 5:

    lastname = str(input("Enter your last name: ")).lower()

    name = name.upper()

    fullname = name + lastname

    print(fullname)

else:
    print(name)
    

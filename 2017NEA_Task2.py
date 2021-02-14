print("Welcome to the fee calculator")

newfee = "y"

while newfee == "y":

    email = str(input("Please enter your email address:  "))
    skill = str(input("Enter your skill level:  ")).upper()
    country = str(input("Enter your country (UK, US, AU):  ")).upper()


    if country == "UK":
        entry = 10
        expert = 35
        casual = 20

        if skill == "E":
            total = entry + expert
            print("The UK dee is: ",total,"GDP")

        elif skill == "C":
            total = entry + casual
            print("The UK fee is: ",total,"GDP")

        else:
            print("Enter the correct skill level")
            skill = str(input("Enter your skill level:  ")).upper()

    elif country == "US":
        entry = 10
        expert = 35
        casual = 20

        if skill == "E":
            total = entry + expert
            total = total * 1.5
            print("The US dee is: ",total,"USD")

        elif skill == "C":
            total = entry + casual
            total = total * 1.5
            print("The US fee is: ",total, "USD")

        else:
            print("Enter the correct skill level")
            skill = str(input("Enter your skill level:  ")).upper()

    elif country == "AU":
            entry = 10
            expert = 35
            casual = 20

            if skill == "E":
                total = entry + expert
                total = total * 2
                print("The AU dee is: ",total,"AUD")

            elif skill == "C":
                total = entry + casual
                total = total * 2
                print("The AU fee is: ",total, "AUD")

            else:
                print("Enter the correct skill level")
                skill = str(input("Enter your skill level:  ")).upper()


    newfee = str(input("Do you want to calculate a new fee? y/n: "))

print("Bye")      

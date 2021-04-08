#Selection05

rain = str(input("Is it raining? ")).lower()

if rain == "yes":
    wind = str(input("Is it windy? ")).lower()

    if wind == "yes":
        print("It's too windy for an umbrella")

    else:
        print("Take an umbrella")

else:
    print("Have a nice day")

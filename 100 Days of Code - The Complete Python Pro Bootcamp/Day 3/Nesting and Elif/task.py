print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("what is your age?"))
    if age <= 18:
       print("you have to pay 7 dollars")

    elif age <= 12:
        print("you have to pay 12 dollars")

    else:
        print('you can ride, pay 5 dollars')


#else:
    #print("Sorry you have to grow taller before you can ride.")

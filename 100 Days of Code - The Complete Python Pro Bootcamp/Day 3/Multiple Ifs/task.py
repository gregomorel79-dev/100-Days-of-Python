print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Please pay $5.")

    elif age <= 18:
        print("Please pay $7.")
        bill =7

    else:
        bill = 12
        print("Please pay $12.")


wants_photo = input("Would you like to see the photo? (y/n)")
if wants_photo == "y":
          # add $3 to their bill
          bill += 3

          print(f"your final bill is: {bill}")





#else:
    #print("Sorry you have to grow taller before you can ride.")

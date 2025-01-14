print("Welcome to Roller Coaster!")

height = float(input("What is your height? "))
if height >= 120:
    print("You can ride.")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print(f"Child ticket is $5")
    elif age <= 18:
        bill = 12
        print(f"Youth ticket is $12")
    else:
        bill = 15
        print(f"Adult bill is $15")
    take_photo = input("Do you want a photo? yes or no? ").lower()
    if take_photo == "y" or take_photo == "yes":
        bill += 3
    print(f"Your final bill is ${bill}")
        
else:
    print("Sorry you cannot ride till you have grow to 120cm.")
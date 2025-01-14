print("Welcome to Python Pizza Deleveries!")
size = input("What size of pizza do you want? L for large, M for medium OR S for small? ").lower()
pepperoni = input("Do you want Pepperoni for your pizza? y or n: ").lower()
extra_cheese = input("Do you want extra cheese? y or n: ").lower()

bill = 0
if size == "l":
    bill += 25
elif size == "m":
    bill += 20
elif size == "s":
    bill = +15
if pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3
if extra_cheese == "y":
    bill += 1
print(f"Your final bill is: ${bill}.")
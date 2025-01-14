
# Print the welcome message
print("Welcome to the tip calculator")

# Collect input from user

total_bill = float(input("What was the total bill? $"))
tip_percent = float(input("How much tip would you like to give? 10, 20, or 30 "))
no_of_people = int(input("How many people is to spluit the bill?"))

# Do the calculation
total_with_tip = total_bill + (tip_percent/100) * total_bill
tip_per_person = total_with_tip/no_of_people

print(f"Each person should pay: ${tip_per_person:.2f}")


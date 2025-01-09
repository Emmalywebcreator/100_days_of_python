# Band Name Generator Project
# Create a greeting for your program.
# Ask the user for the city that they grew up in and store it in a variable.
# Ask the user for the name of a pet and store it in a variable.
# Combine the name of their city and pet and show them their band name


print("Welcome to my Band Name generator App")

city_name = input("What is the name of the city you grew up in?\n")
pet_name = input("What is the name of your pet?\n")

band_name = city_name + pet_name
print(f"Your band name could be {band_name}")
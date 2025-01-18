import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


try:
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
except ValueError:
    print("Invalid input: Please enter a numeric value.")
    exit()

if nr_letters <= 1 or nr_symbols <=1 or nr_numbers <= 1:
    print("Invalid Input: Please enter a number greater than 1 in all field.")
    exit()
else:
    password = []
    for _ in range(nr_letters):
        rand_index = random.randint(0, len(letters) - 1)
        chosen_letters = letters[rand_index]
        password.append(chosen_letters)
        
    for _ in range(nr_symbols):
        chosen_symbols = random.choice(symbols)
        # print(chosen_symbols)
        password.append(chosen_symbols)

    chosen_numbers = random.choices(numbers, k=nr_numbers)
    password.extend(chosen_numbers)
    random.shuffle(password)
    final_password = "".join(password)
    print(f"Your password is: {final_password}")
        
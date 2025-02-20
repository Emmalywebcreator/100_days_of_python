import random


print("Welcome to Number Guessing Game")
print("I'm thinking of a number between 1 and 100")

live = 0
is_game_over = False

level = input("Choose a difficulty. Type e for Easy or h for hard: ").lower()

if level == 'e':
    live += 10
    print(f"You have {live} lives")
elif level == "h":
    live += 5
    print(f"You have {live} lives")
else:
    print("Invalid input. Choose a valid level e for Easy or h for Hard")
    
secret_number = random.randint(1, 100)

while live > 0 and not is_game_over:
    guess = int(input("Make a guess: "))
    if guess > secret_number:
        print("Too high.")
        print("Guess again.")
        live -= 1
        print(f"You have {live} attempts left.")
    elif guess < secret_number:
        print(f"Too low.")
        print("Guess again.")
        live -= 1
        print(f"You have {live} attempts left")
    else:
        print(f"You got it! The number is {guess}")
        is_game_over = True
        
    if live == 0 and not is_game_over:
        print(f"Game over! The number is {secret_number}")

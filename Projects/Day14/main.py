# import data from game_data, logo, vs from art and random from random mosule

import random
from game_data import data
from art import logo, vs
import os

def clr():
     os.system('cls' if os.name == 'nt' else 'clear')

def check_answer(guess, follower_of_account_a, follower_of_account_b):
      correct_answer = "A" if option_a["follower_count"] > option_b["follower_count"] else "B"
      return guess == correct_answer

print(logo)
option_b = random.choice(data)

#print the first object of comparison using random module
score = 0
while True:
    option_a = option_b
    option_b = random.choice(data)
    
    while option_b == option_a:
        option_b = random.choice(data)
    print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}")
    print(vs)
    print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}")

    your_option = input("Who has more follower? type 'A' or 'B'  ").upper()
    clr()
    print(logo)
    
    # if option_a["follower_count"] > option_b["follower_count"]:
    #     if your_option == "A":
    #         score += 1
    #         print(f"You got it right! Your current score  is: {score}")
    #         continue
            
    #     else:
    #         print(f"sorry! you are wrong. Your final score is {score}")
    #         break
    # elif option_b["follower_count"] > option_a["follower_count"]:
    #     if your_option == 'B':
    #         score += 1
    #         print(f"You got it right! Your current score is: {score}")
    is_correct = check_answer(your_option, option_a["follower_count"], option_b["follower_count"])
    if is_correct:
        score += 1
        print(f"Your got it right! Your current score is: {score}")
    else:
        print(f"Sorry! you are wrong. Your final score is {score}")
        break
   






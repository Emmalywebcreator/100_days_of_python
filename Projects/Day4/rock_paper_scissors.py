import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

ascii_art = [rock, paper, scissors]

while True:
    try:
        user_choice = int(input("What did you chose? 0 for rock, 1 for paper or 2 for scissors: "))
        if user_choice not in [0, 1, 2]:
            print("Invalid input: Please enter 0, 1 or 2")
            continue
    except ValueError:
        print("Invalid input: Please enter a number")
        continue

    computer_choice = random.randint(0, 2)

    print(f"\nComputer chose:{["rock", "paper", "scissors"][computer_choice]}")
    print(ascii_art[computer_choice])

    print(f"You chose: {["rock", "paper", "scissors"][user_choice]}")
    print(ascii_art[user_choice])

    if computer_choice == user_choice:
        print("Its a draw!")   
    elif (computer_choice == 0 and user_choice == 2) or \
        (computer_choice == 1 and user_choice == 0) or \
        (computer_choice == 2 and user_choice == 1):
            print("You lose!")
    else:
        print("You win!")
        
    play_again = input("Do you wish to play again? y for yes and n for no: ").lower()
    if play_again != "y":
        print("Thank you for playing")
        break



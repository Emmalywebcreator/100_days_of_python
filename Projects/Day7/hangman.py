import random
from hangman_word import word_list
from hangman_art import logo, stages

print(logo)

chosen_word = random.choice(word_list)
print(f"{chosen_word}")

display = ["_"] * len(chosen_word)
game_over = False
correct_letter = []
lives = 6

while not game_over:
    guess = input("Guess a letter: ")
    
    if guess in correct_letter:
        print(f"You've already guessed '{guess}'. Try another letter.\n")
        continue
    
    correct_letter.append(guess)
    print(correct_letter)
    
    
    if guess in chosen_word:
        print(f"Good guess! '{guess}' is in the word.")
        display = "".join([letter if letter in correct_letter else "_" for letter in chosen_word])
    else:
        lives -= 1
        print(f"Wrong guess! '{guess}' is not in the word. Lives remaining: {lives}")

        
    # Display the current state of the word
    print(f"\nWord: {display}")

    # Check game over conditions
    if "_" not in display:
        game_over = True
        print("\nCongratulations! You've won!")
    elif lives == 0:
        game_over = True
        print(f"\nYou've lost! The word was '{chosen_word}'.")
    
    # Print the current hangman stage
    print(stages[lives])
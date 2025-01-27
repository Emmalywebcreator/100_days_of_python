import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print("Welcome to Hangman Game!")

word_list = ["aardvark", "baboon", "camel", "dog", "fish", "lion", "elephant"]

chosen_word = random.choice(word_list)
print(chosen_word)

word_lenght = len(chosen_word)

# # Create placholder

# placeholder = ""
# for _ in range(word_lenght):
#     placeholder += "_"
# print(placeholder)

# chances = word_lenght
# live = 6
# game_over = False
# correct_answer = []

# while not game_over and chances > 0:
#     guess = input("Guess a letter: ")

#     display = ""
    
#     for letter in chosen_word:
#         if guess == letter:
#             display += letter
#             correct_answer.append(letter)
#             print(stages[live])
#         elif letter in correct_answer:
#             display += letter
#         else:
#             display += "_"
#             live -= 1
#             print(stages[live])
#     print(display)
#     chances -=1
    
#     if "_" not in display:
#         game_over = True
#         print("You won!")
        
        
# if "_" in display and chances < 1:
#     print("You lose")






chances = word_lenght
lives = 6

display = ["_"] * word_lenght

while "_" in display and lives > 0:
    guess = input("Guess a letter: ")

    for position in range(word_lenght):
        if guess == chosen_word[position]:
            display[position] = guess
    
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("You lose")

    print("".join(display))
    print(f"You have {lives} chances left.")
    
    print(stages[lives])
    
if "_" not in display:
    print("You won!")



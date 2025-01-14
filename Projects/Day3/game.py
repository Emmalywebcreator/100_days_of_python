import time
print("Welcome to Haunted House Escape Game!")
print("""
                   !
             lll
          ///     \
         |||       |
 P_______|[][][][][]_______P
++++++++=o0@%@%@%o|||++++++++
|l l l ll [] [] []| l l l l l
|_______| []=== []| |_______|
        |__|| ||___/
        Mystery building
      """)
print("You are trapped in this dark and have only 2 mins to escape")

start_time = time.time()

escape_option = input("Pick an option for escape: door1, door2 or door3? ").lower()

if time.time() - start_time > 20:
    print("You took to much time. Time's up! Game over")
    
if escape_option == "door1":
    print("You enter a room an encounter a dragon to fight")
    pick_a_weapon = input("Pick a weapon: use sword or shield: ").lower()
    
    if time.time() - start_time > 2:
        print("You took to much time. The dragon attacked and defeated you. Game over!")
    
    if pick_a_weapon == "sword":
        print("You foot bravely and defeated the dragon. Congratulation you won!")
        
    else:
        print("You protected yourself, but the dragon fire was too strong. Game over!")
        
elif escape_option == "door2":
    print("You enter a room with a mysterious locked box and a riddle on the wall.")
    print("Riddle: I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?")
    answer = input("Solve the riddle to unlock the box: ").lower()

    # Check time elapsed
    if time.time() - start_time > 20:
        print("You took too long. The room fills with smoke. Game over.")

    if answer == "echo":
        print("Correct! The box opens, revealing a key. You use it to unlock a door leading outside. You escaped successfully!")
    else:
        print("Incorrect answer. The room fills with smoke. Game over.")

    
elif escape_option == "door3":
    print("You enter a room and the floor collapses beneath you!")
    action = input("Quick! Do you grab the rope or try to jump to safety? (rope/jump) ").lower()
    
    if time.time() - start_time > 20:
        print("Time's up! Game over.")
        exit()
        
    if action == "rope":
        print("You grab the rope and climb to safety. You find a door leading outside. You escaped successfully!")
    elif action == "jump":
        print("You attempt to jump, but it's too far. You fall into the abyss. Game over.")
    else:
        print("Invalid choice. You lose your footing and fall. Game over.")

else:
    print("Invalid option. Game over")

# import time

# def start_game():
#     print("Welcome to the Haunted House Escape Game!")
#     print("""
#                        !
#                  lll
#               ///     \\
#              |||       |
#      P_______|[][][][][]_______P
#     ++++++++=o0@%@%@%o|||++++++++
#     |l l l ll [] [] []| l l l l l
#     |_______| []=== []| |_______|
#             |__|| ||___/
#             Katie Buller
#           """)
#     print("You are trapped in a dark house and have only 2 minutes to escape.\n")

#     # Start timer
#     start_time = time.time()

#     # First choice: Choose a door
#     escape_option = input("Choose a door to escape: door1, door2, or door3? ").lower()

#     # Check time elapsed
#     if time.time() - start_time > 120:
#         print("You took too long. Time's up! Game over.")
#         return

#     if escape_option == "door1":
#         room_with_dragon(start_time)
#     elif escape_option == "door2":
#         room_with_puzzle(start_time)
#     elif escape_option == "door3":
#         room_with_abyss(start_time)
#     else:
#         print("Invalid choice. Game over.")

# def room_with_dragon(start_time):
#     print("You enter a room and encounter a dragon!")
#     pick_a_weapon = input("Choose a weapon to fight the dragon: sword or shield? ").lower()

#     # Check time elapsed
#     if time.time() - start_time > 120:
#         print("You took too long. The dragon attacks! Game over.")
#         return

#     if pick_a_weapon == "sword":
#         print("You bravely fight the dragon with the sword and win! You find a hidden passage leading outside. You escaped successfully!")
#     elif pick_a_weapon == "shield":
#         print("You defend yourself with the shield, but the dragon's fire is too strong. Game over.")
#     else:
#         print("Invalid choice. The dragon attacks! Game over.")

# def room_with_puzzle(start_time):
#     print("You enter a room with a mysterious locked box and a riddle on the wall.")
#     print("Riddle: I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?")
#     answer = input("Solve the riddle to unlock the box: ").lower()

#     # Check time elapsed
#     if time.time() - start_time > 120:
#         print("You took too long. The room fills with smoke. Game over.")
#         return

#     if answer == "echo":
#         print("Correct! The box opens, revealing a key. You use it to unlock a door leading outside. You escaped successfully!")
#     else:
#         print("Incorrect answer. The room fills with smoke. Game over.")

# def room_with_abyss(start_time):
#     print("You enter a room and the floor collapses beneath you!")
#     action = input("Quick! Do you grab the rope or try to jump to safety? (rope/jump) ").lower()

#     # Check time elapsed
#     if time.time() - start_time > 120:
#         print("You took too long. You fall into the abyss. Game over.")
#         return

#     if action == "rope":
#         print("You grab the rope and climb to safety. You find a door leading outside. You escaped successfully!")
#     elif action == "jump":
#         print("You attempt to jump, but it's too far. You fall into the abyss. Game over.")
#     else:
#         print("Invalid choice. You lose your footing and fall. Game over.")

# # Start the game
# start_game()

import os

def clear():
    """Clears the terminal screen based on the operating system"""
    os.system('cls' if os.name == 'nt' else 'clear')

# TODO-3: Whether if new bids need to be added
# TODO-2: Save data into dictionary {name: price}
# TODO-1: Ask the user for input


should_continue = True
bid_dict = {}

def find_highest_bidder(bids):
    highest_bid = 0
    winner = ''
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")

while should_continue:
    name = input("What is your name?\n")
    price = int(input("How much are you bidding?\n"))
    bid_dict[name] = price

    new_bidder = input("Are ther any other bidders? 'yes' or 'no'\n").lower()
    if new_bidder == "no":
        should_continue = False
        find_highest_bidder(bid_dict)
    elif new_bidder == "yes":
        should_continue = True
        clear()
    



# TODO-4: Compare bids in dictionary


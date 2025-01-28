import os

def clear():
    """Clears the terminal screen based on the operating system"""
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
bids = {}
bidding_continue = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")
    
while bidding_continue:
    name = input("What is your name?:\n")
    price = int(input("How much do you bid?:\n"))
    bids[name] = price
    should_continue = input("Are there still other bidders?\n yes or no")
    if should_continue == "no":
        bidding_continue = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
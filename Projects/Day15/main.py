from time import sleep
import os


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def clr():
    os.system("cls" if os.name == "nt" else "clear")
def is_resources_successful(ingredient):
    for item in ingredient:
        if ingredient[item] > resources[item]:
            print("Sorry! Not enough ingredient")
            return False
        return True

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money! Money refunded.")
        return False
    
def make_coffee(drink_name, ordered_ingredients):
    for item in ordered_ingredients:
        resources[item] -= ordered_ingredients[item]
    print(f"Here is your {drink_name}. enjoy")
    
def process_coin():
    print("Please insert coin: ")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("how many dimes? ")) * 0.1
    total += int(input("how many nickles? ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

#TODO: 1. On the machine
is_on = True

#TODO: 2. ask user to make their choice and the prompt should show everytime the action is completed 
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    clr()
    #TODO: 3. How t off the machine
    if choice == 'off':
        print("Machine is shutting down...")
        sleep(3)
        print("Goodbye!")
        is_on = False
    elif choice == "report":
        print(f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}ml\nMoney: {profit}$')

    else:
        drink = MENU[choice]
        if is_resources_successful(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
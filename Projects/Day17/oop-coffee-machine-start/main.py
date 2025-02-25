from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    option = menu.get_items()
    choice = input(f"What would you like? {option}: ").lower()
    
    if choice == "off":
        break
    
    elif choice == "report":
        coffee_maker.report()
        
    else:
        drink = menu.find_drink(choice)
        if drink is None:
            print("Invalid choice. Please select a valid drink.")
            continue
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        
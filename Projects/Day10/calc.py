import os
import math
import cmath

def clr():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def add(n1, n2): return n1 + n2
def sub(n1, n2): return n1 - n2
def mul(n1, n2): return n1 * n2
def div(n1, n2): return n1 / n2 if n2 != 0 else "Error, Division by 0 not allowed"
def mod(n1, n2): return n1 % n2 if n2 != 0 else "Error, Modulo by 0 not allowed"
def square(n1): return n1 ** 2
def square_root(n1): return math.sqrt(n1) if n1 >= 0 else cmath.sqrt(n1)

opps = { "+": add, "-": sub, "*": mul, "/": div, "%": mod, "^2": square, "v": square_root}

while True:
    try:
        num1 = float(input("Enter the first number:\n"))
    except ValueError:
        print("Invalid Input: Please enter a valid number.")
        continue
    
    while True:
        print("Available opp:", " ".join(opps.keys()))
        choose_operator = input("Choose an operator:\n")
        
        if choose_operator in opps:
            if choose_operator in ["^2", "v"]:
                result = opps[choose_operator](num1)
                clr()
                print(f"{num1} {choose_operator} = {result}")
            
            
            else:
                try:
                    num2 = float(input("Enter the next number:\n"))
                except ValueError:
                    print("Invalid Input: Please enter a valid number")
            
            
                if choose_operator in ['/', '%'] and num2 == 0:
                    print("Division or modulo by 0 not allowed. Enter a valid number.")
                    continue
                result = opps[choose_operator](num1, num2)
                clr()
                print(f"{num1} {choose_operator} {num2}  = {result}")
        else:
            print("Invalid operation. Please enter a valid operation")
        
        while True:
            choice = input(f"Enter 'y' to continue with {result} 'n' to start afresh 'q' to quit:\n")
            clr()
            if choice == 'y':
                num1 = result
                break
            elif choice == 'n':
                break
            elif choice == 'q':
                print("Goodbye!")
                exit()
        if choice == 'n':
                break     
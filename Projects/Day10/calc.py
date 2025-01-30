def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2
def mod(n1, n2):
    return n1 % n2

operators = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
    "%": mod,
}
num1 = float(input("What is the first number?\n"))

print("Available operoator:", " ".join(operators.keys()))

choose_operator = input("Pick an operator: ")
num2 = float(input("What is the second number?\n"))

if choose_operator == "+":
    print(f"{num1} + {num2} = {operators['+'](num1, num2)}")
elif choose_operator == "-":
    print(f"{num1} - {num2} = {operators['-'](num1, num2)}")
elif choose_operator == "*":
    print(f"{num1} * {num2} = {operators['*'](num1, num2)}")
elif choose_operator == "/":
    print(f"{num1} / {num2} = {operators['/'](num1, num2)}")
elif choose_operator == "%":
    print(f"{num1} % {num2} = {operators['%'](num1, num2)}")








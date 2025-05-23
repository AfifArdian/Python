from art import logo

def add(n1, n2):
    """" add function (+)"""
    return n1 + n2

def subtract(n1, n2):
    """" subtract function (-)"""
    return n1 - n2

def multiply(n1, n2):
    """" multiply function (*)"""
    return n1 * n2

def divide(n1, n2):
    """" divide function (/)"""
    return n1 / n2

def save(n1):
    return n1

operation = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

continue_calculation1 = True
continue_calculation2 = True

def calculator():
    print(logo)
    num1 = float(input("what's the first number?: "))
    while continue_calculation2:
        for v in operation:
            print(v)

        operations_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        result = operation[operations_symbol](num1, num2)

        print(f"{num1} {operations_symbol} {num2} = {result}")

        should_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

        if should_continue == "n":
            # continue_calculation2 = False
            print("\n" * 20)
            calculator()

        elif should_continue == "y":
            num1 = result

calculator()
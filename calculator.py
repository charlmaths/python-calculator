from basicmathoperations import Operators


def basic_operation(operator, num1, num2):
    '''Basic Arithmetic'''
    while operator != 5:
        if operator == 1:
            print("You have chosen to add")
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            adding = Operators(num1, num2)
            res = adding.add()
            print(f"Result: {res}")
            operator = int(input("Another calculation? Enter choice(1/2/3/4/5): "))

        elif operator == 2:
            print("You have chosen to subtract")
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            subtracting = Operators(num1, num2)
            res = subtracting.subtract()
            print(f"Result: {res}")
            operator = int(input("Another calculation? Enter choice(1/2/3/4/5): "))
        elif operator == 3:
            print("You have chosen to multiply")
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            multiplying = Operators(num1, num2)
            res = multiplying.multiply()
            print(f"Result: {res}")
            operator = int(input("Another calculation? Enter choice(1/2/3/4/5): "))
        elif operator == 4:
            print("You have chosen to divide")
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            dividing = Operators(num1, num2)
            res = dividing.divide()
            print(f"Result: {res}")
            operator = int(input("Another calculation? Enter choice(1/2/3/4/5): "))
        else:
            return "Invalid input, exiting..."



def runner():
    ''' initiator '''
    operator = int(input("Enter choice(1/2/3/4/5): "))
    return operator


def main():
    ''' main function '''
    print("Please pick the operation -\n")
    print('''
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Exit
    ''')
    operator = runner()
    basic_op = basic_operation(operator, 0, 0)
    return basic_op


if __name__ == "__main__":
    main()

# print("Exiting the calculator. Goodbye!")





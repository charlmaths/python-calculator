from basicmathoperations import Operators


def basic_operation(operator):
    '''Basic Arithmetic'''
    # num1 = float(input("Enter first number: "))
    # num2 = float(input("Enter second number: "))
    while operator != 5:

        if operator == 1:
            print("You have chosen to add")
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            res = Operators(num1, num2).add()
            print(f"Result: {res}")
            operator = int(input("Another calculation? Enter choice(1/2/3/4/5): "))

        elif operator == 2:
            print("You have chosen to subtract")
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            res = Operators(num1, num2).subtract()
            print(f"Result: {res}")
            operator = int(input("Another calculation? Enter choice(1/2/3/4/5): "))

        elif operator == 3:
            print("You have chosen to multiply")
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            res = Operators(num1, num2).multiply()
            print(f"Result: {res}")
            operator = int(input("Another calculation? Enter choice(1/2/3/4/5): "))

        elif operator == 4:
            print("You have chosen to divide")
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            res = Operators(num1, num2).divide()
            print(f"Result: {res}")
            operator = int(input("Another calculation? Enter choice(1/2/3/4/5): "))

        elif operator == 5:
            print("Exiting...")
            break
        else:
            return "Invalid input, exiting..."



def runner():
    ''' initiator '''
    print("Please pick a calculator:\n")
    print("Calculator Menu:\n")
    print('''
    1. Basic Arithmetic Calculator
    2. Geometric Calculator
    3. Exit
    \n''')
    calc_choice = int(input("Enter choice(1/2/3): "))

    if calc_choice == 1:
        print("Select operation:\n")
        print('''
            1. Add
            2. Subtract
            3. Multiply
            4. Divide
            5. Exit
            \n''')
        operator = int(input("Enter choice(1/2/3/4/5): "))
        return operator

    elif calc_choice == 2:
        print("Geometric Calculator is under development. Exiting...")
        exit()
    elif calc_choice == 3:
        print("Exiting...")
        exit()


def main():
    ''' main function '''
    choice = runner()
    basic_op = basic_operation(choice)
    return basic_op

if __name__ == "__main__":
    main()






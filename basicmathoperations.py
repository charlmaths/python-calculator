# class operators CAREFUL WITH THE NAME
# This class will perform basic math operations on two numbers
# The basic math operations are addition, subtraction, multiplication, and division
'''
How it works:
1. The user is prompted to choose a calculator from the menu.
2. If the user chooses the basic arithmetic calculator, they are prompted to choose an operation (addition, subtraction, multiplication, division) and enter two numbers.
3. The chosen operation is performed on the two numbers and the result is displayed.
4. The user is then prompted to choose another operation or exit the calculator.
5. If the user chooses to exit, the program ends.


'''
class Operators:
    '''Basic Operator Class'''
    def __init__(self,num1,num2):
        '''Constructor Method
        Almost all python classes will have a constructor method. It is used to 'start' or 'initisalised' the class. It is the first method that is called when an object of the class is created/instantiated. It is used to set the initial values of the attributes/variables of the class. You will always see the constructor method defined as __init__(self, ...). The self parameter is a reference to the current instance of the class. It basically contains the 'things' we need for other methods to work.
        '''
        self.num1 = num1
        self.num2 = num2


    def add(self):
        '''Addition Method'''
        return self.num1 + self.num2


    def subtract(self):
        '''Subtraction Method'''
        return self.num1 - self.num2


    def multiply(self):
        '''Multiplication Method'''
        return self.num1 * self.num2


    def divide(self):
        '''Division Method'''
        if self.num2 == 0:
            return "Error: CANNOT DIVIDE BY ZERO"
        return self.num1 / self.num2



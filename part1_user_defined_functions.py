"""
This module contains user defined functions
"""

# def statement used to define the function in python.
# an example follows in the multiline comment
"""
def function_name(parametrs):
    statment(s)
"""


def greet(name):
    print("I am in greeting function")
    """This function greets the name passed to the function. If the passed argument is not string then it is converted to string using __str__ method.

    Arguments:
        name {string} -- [name of the person who is being greeted]
    """
    print("Hello {}".format(str(name)))


greet('Madiyor')
greet('Madiyor Abdukhashimov')


def user_defined_functions(x, y):
    print("I am in user defined functions for max of two numbers")
    """This function returns the max of given two numbers

    Arguments:
        x {int} -- This is any number which is an integer
        y {int} -- This is any number which is an integer
    """
    if int(float(x)) > int(float(y)):
        return x
    return y


max = user_defined_functions(2, 5)
print(max)

# using functions with arbitary number of positional arguments


def my_function(*args):
    print("I am in my_function: for arbitary number of positional arguments")
    """
        This function takes args which is a tuple contains values separated by comma, like tuple
    """
    for i in args:
        print(i)


my_list = [1, 2, 3, 4, 5, 5, 6, 7, 78, 1]
my_function(1, 2, 3, 4, 5, 5, 6, 7,)
print("Calling the function with list")
my_function(*my_list)

# Arbitary number of keyword arguments


def my_kwargs_function(**kwargs):
    print("I am inside the kwargs function")
    """
        This function displays the name: value of the kwargs
        kwargs is dictionary containing keys and the values
    """
    for name, value in kwargs.items():
        print(name, ": ", value)


my_kwargs_function(name='Madiyor', last_name='Abdukhashimov',
                   dob='01.07.1997', email='m.abdukhashimov@edu.com')

# Lambdas
# and example of greeting function which is a inline


def greet_me(): return "Hello"


print(greet_me())

# lambda taking an argument
greet_me_with_name = lambda x="John Doe": print("Hello {}".format(str(x)))

greet_me_with_name("Madiyor Abdukhashimov")

print_all_my_elements = lambda *args: print(*args)
print_all_my_elements(1, 2, 3, 4)


# Function closure
def create_five(x):
    def five():
        return x + 5
    return five


my_five = create_five(5)
my_ten = create_five(10)
print("I was five but closure added another five: ", my_five())
print("I was ten but closure added another five: ", my_ten())


# Nested and return functions example
def fibonacci(n):
    """This is an example of nth fibonacci number

    Arguments:
        n {integer} -- This is the nth fibonnaci number and taken as input from user to

    Returns:
        n {integer} -- nth fibonnaci number
    """
    def step_of_n1_n2(number1, number2):
        return number2, number1 + number2
    number1, number2 = 0, 1
    for i in range(n):
        number1, number2 = step_of_n1_n2(number1, number2)
    return number1


print("Tenth Fibonnaci number: ", fibonacci(10))

# An example of recursive calculating nth factorial


def nthfactorial(number):
    """nthfactorial - calulates the nth factorial of given user number as an input (recursive function)

    Arguments:
        number {integer} -- It is the requested factorial number of nth

    Returns:
        number - {integer} -- Returns the nth factorial number
    """
    if number == 0:
        return 1
    else:
        return number*nthfactorial(number-1)


# An Example of creating 5th factorial using recursive function
print("5th factorial: ", nthfactorial(5))

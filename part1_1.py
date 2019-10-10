# Very first program 'Hello World'
print("Hello World")
# This is a line comment in python
"""
This is the multiline comment and can even be used for built in documentation.
"""

# naming convensions...
# name should start with underscore or alphabets
# name identifiers are case sensitive.
# special names starts with double underscore and end with double underscore
# For Example Special function: def __init__(self, *args, **kwargs)

# More About Naming Convensions...
# Module and package names are  - all lowercase.
# Globals and Constants are     - all UPPERCASE
# Classes are Bumpy caps        - with initial upper.
# Methods and functions         - all lowercase seperated with underscores
# variable names                - all lowercase separated with underscores or bumpy case with initial lowercase

# Some Samples for above given commented instructions


class SomeThing(object):
    '''
    Here Comes the multiline comment
    which can be used for building documentaton.
    with the following like way
    SomeThing.__doc__

    '''
    __i_am_private = 'I am a private string'
    _i_am_protected = 'I am a protected string'

    def __init__(self, *args, **kwargs):
        '''THis is also multi line comment and can be used for documenting functions'''
        pass

    def this_is_my_function(self):
        '''Here is another comment
            Defines the function and its naming convension'''
        pass

    @staticmethod
    def i_am_static_method(x):
        print(x)
        pass


def hello_world_function():
    print("Hello World from part1_1.py module")


'''
Python string operations
'''


def is_this_string(name):
    if type(name) == str:
        return "%r is a string." % (name)
    name = str(name)
    return "%r is not a string." % (name)


name = "Madiyor Abdukhashimov"
join_str = "Ha"
print(name)
print(is_this_string(name))
print(is_this_string(12))


# String operations in python
print("This is capitalized string: ", name.capitalize())
print("This is centeralized string: ", name.center(len(name)*2, '~'))
print("This is a casfold string: ", name.casefold())
print("This is a lowecase string: ", name.lower())
print("This is a string occurance count: ", name.count("a"))
print("This is a string endwith check: ", name.endswith("ov"))
print("This finds the first occurance of a character in the string: ", name.find("a"))
print("This is formatted string and here is your name: {}".format(name))
print("This is an exaple of string join: ", name.join(join_str))
print("Left justified string example: ", name.ljust(len(name)*2, '~'))
print("Right justified string example: ", name.rjust(len(name)*2, '~'))
print("Swapcase string example: ", name.swapcase())
print("Example of removing first leading character: ", name.lstrip('Ma'))
print("Example of removing trailing character: ", name.rstrip("ov"))
print("Example of making tuple out of string: ", name.partition("a"))
print("Example of making the string sorted: ", sorted(list(name)))

'''Python Variable exaples'''

'''
Variables can be considered as a storage container. It can be used to store information
'''

'''
Python convention is as follows
'variable name' = 'value or information' 
'''

# Usage of an integer
speed_of_car = 350
# Usage of a string in python
name_of_car = 'Ferrari'
print('{} can be fas as {} km/h'.format(name_of_car, speed_of_car))

# In python everyting is an object and type is an instance of an object in python
# Data types of variables is determined by Python interpreter by assignment like variable = value

# Printing the type of a variable is done by using type function
float_example = 12.1023
this_is_list = list('Madiyor Abdukhashimov')
this_is_set = set('Mirzashamol Karshiev')
this_is_dict = dict.fromkeys(this_is_set, this_is_set)
print(type(speed_of_car))
print(type(name_of_car))
print(type(float_example))
print(type(bin(14)))
print(type(this_is_list))
print(type(this_is_set))
print(type(this_is_dict))

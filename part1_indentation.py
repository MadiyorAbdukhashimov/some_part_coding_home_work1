# Indentation examples
"""
This module contains examples for indentations.
"""

class Something(object):
    """ Every function or variable belonging to this class
        Must Be indeneted equally with 4 spaces.
        examples as follows
    """
    name = 'Madiyor'
    last_name = 'Abdukhashimov'
    __email = 'm.abdukhashimov@edu.com'

    # function is indented as required for class Something scope
    def __init__(self, name, last_name, email, *args, **kwargs):
        # Everything belonging to this function must be indented as the same follows
        self.name = name
        self.last_name = last_name
        self.__email = email

    def some_function(self, x, y):
        # Notice everything belonging to this function must be indented
        if x > y:
            return x
            print('I have returned x') # Notice this line will not be executed
        return y

def another_function(x, y):
    # Notice if the function is not indented then it is not gonna belong to the classs.
    pass

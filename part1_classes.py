"""
This module contains the examples of Class, Inheritance, and Polymorphysim
"""


class Person(object):
    """ Person class defines the person object and includes the
        first and last name, and email
    """

    def __init__(self, first_name='John', last_name="Doe",
                 email="johndoe@gmail.com"):
        """ __init__ - constructor function and
            initializes first, last names and email

        Keyword Arguments:
            first_name {str} -- [description] (default: {'John'})
            last_name {str} -- [description] (default: {"Doe"})
            email {str} -- [description] (default: {"johndoe@gmail.com"})
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def get_first_name(self):
        """function returns the first name of the person

        Returns:
            first_name -- the first name of the Person
        """
        return self.first_name

    def get_last_name(self):
        """Function returns the last name of the person

        Returns:
            last_name -- string, the last name of the Person
        """
        return self.last_name

    def get_email(self):
        """Function returns the email of the Person

        Returns:
            str -- email of the Person
        """
        return self.email


Madiyor = Person('Madiyor', 'Abdukhashimov', 'm.abdukhashimov@edu.com')
print("first name: \t", Madiyor.get_first_name())
print("last name: \t", Madiyor.get_last_name())
print("email: \t\t", Madiyor.get_email())

# Inheritance


class Car(object):
    """ Car class is the base class which is created to be inherited by other
        classes.
        object  -- it is also inheriting from object class, which is the
        convention for class for python3.*
        It has one public var called name which is a string
    """
    name = 'car'

    def __init__(self, color):
        """ constructor of Car class takes the color as an argument,
            which is required and has no default value

        Arguments:
            color {string} -- the color of the car, for ex: 'black'
        """
        print('Inside the Car class')
        self.color = color

    def get_color(self):
        """Function that returns the color of the car

        Returns:
            string -- the color of the car, for ex: 'red'
        """
        return self.color

    def get_name(self):
        """ The function which returns the name of the car,
            the name of the car is a global variable provided in the class

        Returns:
            string -- the name of the car, for ex: 'Ferrari'
        """
        return self.name


class Ferrari(Car):
    """ The class Inherits from Car.
        Ferrari is a Car relationship holds between them.
    """
    # overriding the public variable name
    name = 'Ferrari'

    def __init__(self, color):
        # constructor function which calls the super function
        # to initialize the color variable
        super(Ferrari, self).__init__(color)


class BMW(Car):
    """The class Inherits from Car. BWM is a Car relationship holds between them.
    """
    # overriding the public variable name
    name = 'BMW'

    def __init__(self, color):
        # constructor function which calls the super function
        # to initialize the color variable
        super(BMW, self).__init__(color)


class Ravon(Car):
    """The class Inherits from Car. Ravon is a Car relationship holds between them.
    """
    # overriding the public variable name
    name = 'Ravon'

    def __init__(self, color):
        # constructor function which calls the super function
        # to initialize the color variable
        super(Ravon, self).__init__(color)


# instantiating the Cars
my_cars = [
    Ferrari('red'),
    BMW('blue'),
    Ravon('black')
]
# displaying the properties of cars
for my_car in my_cars:
    print("This car is {} and its color is {}".format(
        my_car.get_name(), my_car.get_color()))

# Polymorphism


class Animal(object):
    """Animal class has some properties which is to be inherited and
    Raises:
        walk -  NotImplementedError: [inheriting object must implement this method]
                defines the walking speed
        says -  NotImplementedError: [inheriting object must implement this method]
                defines the sound of the animal
        likes - NotImplementedError: [inheriting object must implement this method]
                defines the favorite food of the animal
    """

    def __init__(self, name):
        """contstructor function for Animal

        Arguments:
            name {string} -- the name of the animal, required argument
        """
        self.name = name

    def walk(self):
        """function supposed to return the walking speed of the animal

        Raises:
            NotImplementedError: it must be implemented in inheriting class
        """
        raise NotImplementedError(
            'Sub class must implement this abstract method')

    def says(self):
        """function supposed to return the sound of the animal, which is a string

        Raises:
            NotImplementedError: it must be implemented in inheriting class
        """
        raise NotImplementedError(
            'Sub class must implement this abstract method')

    def likes(self):
        """function supposed to return the fav food of the animal, which is a string

        Raises:
            NotImplementedError: it must be implemented in inheriting class
        """
        raise NotImplementedError(
            'Sub class must implement this abstract method')


class Dog(Animal):
    """Dog class is an Animal
    Arguments:
        Animal {object} -- inherited from Animal class
    """

    def __str__(self):
        # overriding __str__ method
        return "dog"

    def walk(self):
        # implementing walk method according to the Dog class
        return 25

    def says(self):
        # implementing says method according to the Dog class
        return "ruff-ruff"

    def likes(self):
        # implementing likes method according to the Dog class
        return "meat"


class Cat(Animal):
    """
    Cat is an Animal
    """

    def __str__(self):
        return "cat"

    def walk(self):
        # implementing walk method according to the Cat class
        return 20

    def says(self):
        # implementing says method according to the Cat class
        return "meaow"

    def likes(self):
        # implementing likes method according to the Cat class
        return "milk"


class Cow(Animal):
    """
    Cat is an Animal
    """

    def __str__(self):
        return 'cow'

    def walk(self):
        # implementing walk method according to the Cow class
        return 40

    def says(self):
        # implementing says method according to the Cow class
        return "Moooou"

    def likes(self):
        # implementing likes method according to the Cow class
        return "Fresh Grass"


animals = [
    Dog('Fido'),
    Cat('Guido'),
    Cow('Ferd')
]

for animal in animals:
    print("{} is a {}, and says {}. Walks with speed of {} km/h, and likes eating".format(
        animal.name, str(animal), animal.says(), animal.walk(), animal.likes()
    ))

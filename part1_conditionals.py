"""
This module contains conditional examples
"""

number = 10

result = "Greater than 10" if number > 10 else "Smaller than or equal to 10"
print(result)

my_second_number = 100
if my_second_number > 100:
    print("This is greater than 100")
elif (my_second_number == 100):
    print("This is equal to 100")
else:
    print("This is smaller than 100")


name = 'Madiyor'

if len(name) < 10:
    print("Your name length is smaller than 10")
    if name[0] == 'C':
        print("Your name starts with C")
    elif name[0] == 'M':
        print("Your name starts with M")
        if name [1] == 'a':
            print("Your name's second character is a")
    else:
        print("See what is your names first character yourself")
        print("Your name: ", name[0])
else:
    print("Your name length is greater or equal to 10")
    if name[0] == 'A':
        print("Your name starts with A")
    elif name[0] == 'B':
        print("Your name starts with B")
    elif name[0] == "M":
        print("Your name starts with M")
    else:
        print("I do not know your names first character")
        print("Look and find yourself")
        print(name[0])

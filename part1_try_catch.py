"""
This module contains Exeption handling
"""

# opening the file does not exist and raising an Exception with the Message

# Writing the custom message for error
try:
    f = open('testfile.txt')
except Exception:
    print('Seems like the file does not exist in the current folder')


# catching more than one Exceptions
try:
    f = open('test_file.txt')
    var = not_created_car
except FileNotFoundError:
    print('Seems like the file does not exist in the current folder')
except Exception as e:
    print(e)


try:
    f = open('test_file.txt')
except FileNotFoundError as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing the finally")

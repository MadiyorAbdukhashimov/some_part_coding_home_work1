'''
Module contains examples of python operators
'''

number1 = 2060
number2 = 5700

# plus operator in python example
result = number1 + number2
print("{} + {} = ".format(number1, number2), result)

# minus operator in python example
result = number1 - number2
print("{} - {} = ".format(number1, number2), result)

# * operator in python example
result = number1 * number2
print("{} * {} = ".format(number1, number2), result)

# / operator in python example
result = number1 / number2
print("{} / {} = ".format(number1, number2), result)


# // operator in python example
result = number2 // number1
print("{} // {} = ".format(number2, number1), result)

# ** operator in python example
result = (number1//1000) ** (number2//1000)
print("{} ** {} = ".format(number1, number2), result)
''' ** works the same as power function'''


# % operator in python example
result = number1 % 21
print("{} % {} = ".format(number1, 21), result)

# short hand notations +=, -=, *=, /= ...

my_number = 1024

my_number += 1024
print("my_number +=1024: ", my_number)

my_number -= 512
print("my_number -=512: ", my_number)

my_number *= 16
print("my_number *=16: ", my_number)

my_number /=4
print("my_number /= 4 :", my_number)

my_number //= 2
print("my_number //=2 : ", my_number)

my_number %= 5
print("my_number %=5: ", my_number)

my_number **= 4
print("my_number **=4: ", my_number)

my_number1 = 10
my_number2 = 12

# Output: my_number1 > my_number2 is False
print('my_number1 > my_number2  is',my_number1>my_number2 )


# Output: my_number1 < my_number2 is True
print('my_number1 < my_number2  is',my_number1<my_number2 )


# Output: my_number1 == my_number2 is False
print('my_number1 == my_number2 is',my_number1==my_number2 )


# Output: my_number1 != my_number2 is True
print('my_number1 != my_number2 is',my_number1!=my_number2 )


# Output: my_number1 >= my_number2 is False
print('my_number1 >= my_number2 is',my_number1>=my_number2 )


# Output: my_number1 <= my_number2 is True
print('my_number1 <= my_number2 is',my_number1<=my_number2 )

# Booleans


boolean1 = True

boolean2 = False

# Output: boolean1 and boolean2 is False
print('boolean1 and boolean2 is',boolean1 and boolean2)

# Output: boolean1 or boolean2 is True
print('boolean1 or boolean2 is',boolean1 or boolean2)

# Output: not boolean1 is False
print('not boolean1 is',not boolean1)


first_number = 102 
second_number = 29       
result = 0

result = first_number & second_number; 
print ("Line 1 - Value of c is ", bin(result))

result = first_number | second_number;  
print ("Line 2 - Value of c is ", bin(result))

result = first_number ^ second_number;
print ("Line 3 - Value of c is ", bin(result))

result = ~first_number ;
print ("Line 4 - Value of c is ", bin(result))

result = first_number << 2 ;
print ("Line 5 - Value of c is ", bin(result))

result = first_number >> 2 ;
print ("Line 6 - Value of c is ", bin(result))

# not in operator example
print("Not fibonacci numbers".title())
list = [1, 2, 3, 4, 5, 6, 7, 8]
for i in list:
    if not i in (1, 2, 3, 5, 8):
        print(i)
print("Fibonnaci numbers".title())
for i in list:
    if i in (1, 2, 3, 5, 8):
        print(i)
# identity

a = 20
b = 40
if a is b:
    print("A and B have the same identity")
else:
    print("A and B do not have the same identity")

a = 40

if a is not b:
    print("A and B do not have the same identity")
else:
    print("A and B have the same identity")

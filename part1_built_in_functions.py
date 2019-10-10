# To know functoinality of any function we can use help
# An example as follows
import math
help(max)

# Built in modules contain extra functionalities, As an example, in order to calculate the square root of a number, we need to import math module
# Example as follows
help(math.sqrt)
# prints the square root of the given number, example: 1002
print(math.sqrt(1002))

# in order to find the absalute value of the number we can use built in abs function
negativeNumber = -1111111
absoluteValueOfNegNumber = abs(negativeNumber)
print("I was negative: ", negativeNumber)
print("Now I turned positive: ", absoluteValueOfNegNumber)

# we can round the number. for example 2.5 = 2
round_me = 2.5
print(round(round_me))
# round function gives the rough value for the given input

# we can use the ceiing and floor options with the help of math functions
number_floorme = 2.3
number_ceilme = 4.6
print("I have been flooerd: ): ", math.floor(number_floorme))
# math floor functions calculates the floor of the given number

print("I have been ceiled by mat module: ", math.ceil(number_ceilme))
#  math ceil function calculates the ceil of the given input/ number

# parsing the numbers to str, str to number, float can be done as follows
iAmNumber = '145.123'
print("Now I am an Integer value: ", int(float(iAmNumber)))
print("Now I am a floating value: ", float(iAmNumber))
print("Now I am a list: ", list(iAmNumber))
print("Now I am a set:", set(iAmNumber))
print("Now I am a dictionary", dict.fromkeys(set(iAmNumber), set(iAmNumber)))

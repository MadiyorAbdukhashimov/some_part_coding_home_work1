"""
This module contains looping constraints
"""

# break statement -
# when break gets executed flow breaks out immediately

i = 0
while (i < 7):
    print(i)
    if i == 4:
        print("Now break gets executed")
        print("Stay readyyyyy")
        print("BREAAAAK")
        break
    i += 1

# the same idea inside for loop

for i in range(0, 7):
    print(i)
    if i == 4:
        print("Breaking get readyyyy")
        print("BREAAAK")
        break


# continute statement skips the loop

for i in range(0, 10):
    if i == 2 or i == 4:
        print("Look I skip the {} xa xa".format(i))
        continue
    print(i)

# nested for loops
print("I will print the square", end="\n")

for i in range(0, 5):
    for j in range(0, 5):
        print("*", end=" ")
    print("")

print("")

print("I will print rectangle", end="\n")

for i in range(0, 2):
    for j in range(0, 5):
        print("*", end=" ")
    print("")
print("")

for i in range(0, 5):
    for j in range(0, 2):
        print("*", end=" ")
    print("")
print("")

name_list = list('Madiyor Abdukhashimov')
# print every single character inside the name list
for i in name_list:
    print(i, end=", ")
print("")

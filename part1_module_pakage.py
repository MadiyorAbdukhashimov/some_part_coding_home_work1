try:
    # tries to open the file to read its contents
    fread = open('test_file.txt', 'r')
except FileNotFoundError as e:
    # prints the error message
    print(e)
else:
    # opening the file and reading its content
    print(fread.read())
    fread.close()


try:
    # tries to open the file to append to its contents
    fwrite = open('test_file.txt', 'a')
except FileNotFoundError as e:
    # Prints the error message to the standart ouput
    print(e)
else:
    # writes the string to the file
    fwrite.write('Madiyor')
    fwrite.close()


# writing the integer to the file
try:
    fwrite = open('test_file.txt', 'a')
except FileNotFoundError as e:
    print(e)
else:
    fwrite.write("\nThis was the integer: {}".format(1))
    fwrite.close()


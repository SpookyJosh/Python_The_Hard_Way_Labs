#imports the 'argv' feature from the sys module
from sys import argv
#Defines arguments named 'script' and 'input_File' and assigns them to argv
script, input_file = argv
#Creates function 'print_all' and defines argument 'f'
#Function prints the variable f with the '.read()' method
#which makes the file readable in memory
def print_all(f):
    print(f.read())
#Creates function 'rewind' with argument 'f'
#Function issues 'seek()' method with value of '0' on 'f'
#Seek Returns an open file to the specified byte number, 0 means the beginning
def rewind(f):
    f.seek(0)
#Creates function 'print_a_line' with arguments 'line_count' and 'f'
#Function prints the variable 'line_count' followed by 'f' with the 'readline()' method
#Finally the 'end""' tells print to exclude the '\n' that readline() would end with
def print_a_line(line_count, f):
    print(line_count, f.readline(), end="")
#Runs the 'open' function on variable 'input_file' and assigns it to variable 'current_file'
current_file = open(input_file)
#Prints string "First let's print the whole file" and ends with \n to create a new line
print("First let's print the whole file:\n")
#Runs function 'print_all' and supplies 'current_file' as the argument - this will read the specified file on screen
print_all(current_file)
#prints sting 'Now let's rewing, kind of like a tape'
print("Now let's rewind, kind of like a tape")
#Runs function 'rewind' and supplies 'current_file' as the argument - Runs the seek method against the specified file to return to the beginning
rewind(current_file)
#Prints string 'Let's print three lines:'
print("Let's print three lines:")
#Assigns integer value '1' to variable 'current_line'
current_line = 1
#Runs function 'print_a_line' and supplies arguments 'current_line' and 'current_file'
#This prints the value of 'current_line and then executes the readline() method on the specified file, printing the current line and taking you to the next line
print_a_line(current_line, current_file)
#Assigns the value of 'current_line +1' to variable 'current_line'
current_line += 1
#Executes function 'print_a_line' which will print the next line in the same file and include the number 2 at the beginning
print_a_line(current_line, current_file)
#Adds 1 to current_line and assigns it
current_line += 1
#Executes function 'print_a_line'  with '3' at the beginning followed by the 3rd line of the file
print_a_line(current_line, current_file)

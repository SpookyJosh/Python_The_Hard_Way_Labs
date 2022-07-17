#import argv from sys module
from sys import argv
#define arguments script and filename for argv
script, filename = argv
#Assign the 'open' function to variable text and use it to open filename
txt = open(filename)
#print f-strings 'here's your file' and insert filename variable
print(f"Here's your file {filename}:")
#print contents of variable text with the method 'read' to print file contents
print(txt.read())
#closes open file
txt.close()
#print string 'type the filename again:'
print("Type the filename again:")
#Assign input function with a '>' character to variable 'file_again'
file_again = input("> ")
#assign function 'open' with 'file_again' file to variable txt_again
txt_again = open(file_again)
#print 'txt_again' with the .read method to print file content
print(txt_again.read())
#closes open file
txt_again.close()

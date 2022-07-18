from sys import argv
script, filename = argv

file = open(filename, 'r')

print(f"Let's read the file {filename}:")
print(file.read())

print(f"=====\nNow let's close the file")
file.close()

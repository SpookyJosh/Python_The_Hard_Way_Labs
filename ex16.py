from sys import argv
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN")

input("Press Return To Proceed: ")

print("Opening the file...")
target = open(filename, 'a')

print("Truncating the file. Goodbye!")
target.truncate(0)

target.close()

target = open(filename, 'a')


print("Now I'm going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to a file")

target.write(f"{line1}\n{line2}\n{line3}")
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print("And finally, we close it")
target.close()

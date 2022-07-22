#this one is like your scripts with argv
def print_two(*argy):
    arg1, arg2 = argy
    print(f"arg1: {arg1}, arg2: {arg2}")

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#This just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#This one takes no arguments
def print_none():
    print("I got nothin'.")

print_two("Josh","Smith")
print_two_again("Nice","Mean")
print_one("Single")
print_none()

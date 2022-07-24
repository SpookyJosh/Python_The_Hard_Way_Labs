from sys import argv
script, flava1, flava2 = argv
#def skittles(flavor1, flavor2, flavor):
#    print(f"We have the following flavors: {flavor1}, {flavor2}, and {flavor3}")

def skittles(*flaves):
    flavor1, flavor2 = flaves
    print(f"We have two flaves: {flavor1} and {flavor2}")

#first = input("Enter first flavor: ")
#second = input("Enter your second flavor: ")
#third = input("Enter your third flavor: ")

#skittles(first, second, third)

#skittles("red", "green", "yellow")

#skittles(input("Enter your first flavor: "), input("Enter your second flavor: "), input("Enter your third flavor: "))
skittles(flava1, flava2)

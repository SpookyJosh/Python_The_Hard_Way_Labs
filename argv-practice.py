from sys import argv

script, fruit, vegetable, meat, carb = argv

print(f"So, you're favorite fruit is {fruit} and your favorite vegetable is {vegetable}")
print(f"Also, your favorite meat is {meat} and your favorite carb is {carb}")

more = input("Gimme some more: ")
print(f"This is whatcha gave me: {more}")
print("This is whatcha gave me: ", more)

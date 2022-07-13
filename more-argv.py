from sys import argv
script, num1, num2 = argv

add = int(num1) * int(num2)
print(f"""
So you entered {num1} and {num2}
Those two numbers multiplied equals {add}
""")

#assigns string value '{} {} {} {}' to variable named 'formatter'
formatter = "{} {} {} {}"
#prints '1 2 3 4' by format function subsituting 1,2,3 and 4 into 'formatter'
print(formatter.format(1, 2, 3, 4))
#prints 'one two three four' by format function
print(formatter.format("one", "two", "three", "four"))
#prints 'True False False True' boolean values using format function
print(formatter.format(True, False, False, True))
#prints '{} {} {} {}' four times substituting formatter's value into itself
print(formatter.format(formatter, formatter, formatter, formatter))
#prints 'Hello World; Momma, I'm writing' code; Just you watch, this code will be great!!; You never know if you don't try, right?''
print(formatter.format(
    "Hello World; ",
    "Momma, I'm writin' code; ",
    "Just you watch, this code will be great!!; ",
    "You Never know if you don't try, right?"
))

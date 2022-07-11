#assigns integer '10' to variable
types_of_people = 10
#assigns string using f-string format 'There are 10 types of people'
x = f"There are {types_of_people} types of people."
#assigns string 'binary' to variable
binary = "binary"
#assigns string "don't" to variable
do_not = "don't"
#assigns string 'Those who know binary and those who don't' to variable
y = f"Those who know {binary} and those who {do_not}."
#print 'there are 10 types of people'
print(x)
#prints 'Those who know binary and those who don't'
print(y)
#prints 'I said: There are 10 types of people'
print(f"I said: {x}.")
#Prints 'I also said: Those who know binary and those who don't'
print(f"I also said: '{y}'")
#assigns boolean 'False' to variable
hilarious = False
#assigns string 'Isn't that joke so funny?! {}' to variable
joke_evaluation = "Isn't that joke so funny?! {}"
#prints 'Isn't that joke so funny?! False' - {} takes value of variable 'hilarious'
print(joke_evaluation.format(hilarious))
#assigns 'this is the left side of...' to variable
w = "This is the left side of..."
#assigns 'a string with a right side' to variable
e = "a string with a right side."
#prints 'This is the left side of...a string with a right side'
print(w + e)

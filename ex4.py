#Assigns integer '100' to variable named cars
cars = 100
#Assigns float '4.0' to variable named space_in_a_car
space_in_a_car = 4.0
#Assigns integer '30' to variable named 'drivers'
drivers = 30
#Assigns integer '90' to variable named 'passengers'
passengers = 90
#Assigns value 'cars minus drivers' which is '70' to variable named 'cars_not_driven'
cars_not_driven = cars - drivers
#Assigns value 'drivers' which is '30' to variable named 'cars_driven'
cars_driven = drivers
#Assigns value 'cars_driven times space_in_a_car' which is '120.0' to a variable named 'carpool_capacity'
carpool_capacity = cars_driven * space_in_a_car
#Assigns value 'passengers divided by cars_driven' which is '3' to variable named 'average_passengers_per_car'
average_passengers_per_car = passengers / cars_driven
#Prints 'There are 100 cars available'
print('There are', cars, 'cars available.')
#Prints 'There are only 30 drivers available'
print('There are only', drivers, 'drivers available.')
#Prints 'There will be 70 empty cars today'
print('There will be', cars_not_driven, 'empty cars today.')
#Prints 'We can transport 120.0 people today'
print('We can transport', carpool_capacity, 'people today.')
#Prints 'We have 90 to carpool today'
print('We have', passengers, 'to carpool today')
#Prints 'We need to put about 3.0 in each car'
print('We need to put about', average_passengers_per_car, 'in each car.')

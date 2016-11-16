# -*- coding: utf-8 -*-

# There are 100 cars
cars = 100
# Every car has 4.0 seats
space_in_a_car = 4.0
# There are total 30 drivers
drivers = 30
# There are total 90 passengers
passengers = 91
# how many cars have no driver, cars number substracs the drivers number
cars_not_driven = cars - drivers
# how many cars have drivers
cars_driven = drivers
# The total space that can be used is cars_driven * space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# The average number in a car is the passengers num divided by the number of cars driven
average_passengers_per_car = passengers / cars_driven

print "There are ", cars, " cars avaliable."
print "There are only ", drivers," drivers avaliable."
print "There will be ", cars_not_driven, " empty car today."
print "We can transport ", carpool_capacity, "people today."
print "We have ", passengers, "people to carpool today."
print "We need to put about ", average_passengers_per_car, " in each car."

print "Hello %s." % "小明" 

# -*- coding: utf-8 -*-

cars = 100
space_in_a_car = 4.111
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are %d cars avaliable." % cars)
print("There are only ", drivers, "drivers avaliable.")
print("There will be ",cars_not_driven, " empty cars today.")
print("We can transport ", passengers, " people today.")
print("We have %f to carpool today." % carpool_capacity)
print("We need to put about ",average_passengers_per_car, " in each car.")

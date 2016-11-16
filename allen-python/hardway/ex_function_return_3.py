# -*- coding: utf-8 -*-

first_num = float(input("first num: "))
second_num = float(input("second num: "))

def add(a, b):
    print("ADDING %f + %f." % (a, b))
    return a + b

def subtract(a, b):
    print("SUBTRACT %f - %f." % (a, b))
    return a - b

def multiply(a, b):
    print("Multiply %f * %f." % (a, b))
    return a * b

def divide(a, b):
    print("DIVIDING %f / %f." % (a, b))
    return a / b

print("Result of adding is :", add(first_num, second_num))
print("Result of subtracting is :", subtract(first_num, second_num))
print("Result of multipling is :", multiply(first_num, second_num))
print("Result of dividing is: ", divide(first_num, second_num))

# make a formula : 1 + 2 * 4 - 5 / 2
result = subtract(add(1,multiply(2, 4)),divide(5, 2))
print("Result of the formula is :", result)

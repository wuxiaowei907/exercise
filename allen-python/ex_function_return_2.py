# -*- coding: utf-8 -*-

def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBSTRACT %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "Multiply %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do something with just functions!"

age = add(30, 3)
height = subtract(183, 4)
weight =  divide(85, 2)
iq = divide(200, 3)

print "Age: %d, Height: %d, weight: %d, IQ: %d" % (age, height, weight, iq)

print "Here is puzzle."
what = add(age, subtract(height, multiply(weight,divide(iq,2))))

print "That becomes: ", what, "Can you do it by hand?"

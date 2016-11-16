# -*- coding: utf-8 -*-

print "1.How old are you?",
age = raw_input()
print "1.How tall are you?",
height = raw_input()
print "1.how much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

print "let's do again",'*' * 15

age = raw_input("2.How old are you? ")
height = raw_input("2.How tall are you? ")
weight = raw_input("2.How much do you weight? ")

print "So,again you're %r old, %r tall and %r heavy." % (age, height, weight)

# dd = "skk"
# # python2,if input a string, it will be as a veriable name
# # eg. if input dd ,the eyes = "skk"
# eyes = input("How many eyes do you have?")
# print(type(eyes))
# print("eyes: %r" % eyes) #

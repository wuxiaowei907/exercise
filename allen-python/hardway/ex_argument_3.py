# -*- coding: utf-8 -*-

from sys import argv

script, first, second, third = argv

print("The script is called: ", script)
print("The first variable is: ", first)
print("The second variable is: ", second)
print("The third variable is: ", third)

print("The script is called: %r" % script)
print("The first variable is: %r" % first)
print("The second variable is: %r" % second)
print("The third variable is: %r" % third)

a,b = 1, 3
print(a, "\t", b)
l = ["a","b","c"]
v1, v2, v3 = l
print(v1,v2,v3,sep = '\t')

other_input_value = input("Input anything you want: ")
print("The other way to get intput data: ",other_input_value)

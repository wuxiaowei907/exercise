# -*- coding: utf-8 -*-

def print_two(*args):
    arg1, arg2 = args
    print("arg1=",arg1,", arg2 = ",arg2)

def print_two_again(arg1, arg2):
    print("arg1 = %r, arg2 = %r" % (arg1, arg2))

def print_one(arg1):
    print("arg1 = %r" % arg1)

def print_none():
    print("I doing nothin!")

print_two("Mecheal", "Allen")
print_two_again("Mia", "Kevin")
print_one("xiaoming")
print_none()

# -*- coding: utf-8 -*-

from sys import argv

# if(len(argv) != 2):
#     print("usage: python3 ex_file_v1_3.py filename")
#     # how to exit the process??
#
# script, filename = argv
#
# txt = open(filename)
# print(type(txt))
# print("This is the file %r:" % filename)
# print("The content is : %r" % txt.readline())

filename_again = input("Type the filename again: \n> ")
txt_again = open(filename_again)

print(txt_again.read())

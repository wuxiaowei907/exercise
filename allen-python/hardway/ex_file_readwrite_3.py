# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

print("We are going to erase %s." % filename)
print("If you don't want do that, hit CTRL + C(^C).")
print("If you want do that, hit RETURN.")
input("?")

print("Opening the file ....")
target = open(filename, 'w')

print("Truncating the file...")
target.truncate()

print("Now, I'm going to ask you to input three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("Now, I will write these in the file.")
# target.write(line1)
# target.writelines(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print("And finally, I will close file.")
target.close()

# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

print "I'll erase the file %r." % filename
print "If you don't want do that, hit CTRC + C (^C)."
print "If you want do that, hit Return."

raw_input("?")

print "Opening the file ..."
# the model will affect the
# funciton invokeed result,must keep that in mind
target = open(filename, 'w+')
print target.read() # print nothing
print "begin to truncate file, goodbye!"
target.truncate()

print "Now I'm going to ask you to input 3 lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "Now I will write these into the %s" % filename

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3);
target.write("\n")

print "And finally, we close it."
target.flush()

target.close()

# print target.read() #[Errno 9] Bad file descriptor

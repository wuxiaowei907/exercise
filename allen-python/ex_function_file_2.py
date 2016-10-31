# -*- coding: utf-8 -*-

from sys import argv

script, file_name = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def rewind_with_offset(f, offset):
    f.seek(offset, 1)

def print_a_line(line_count, f):
    # print "The line_count is %r." % line_count
    print line_count, f.readline(),

current_file = open(file_name)

print "First, Let's print the whole file: "
print_all(current_file)

print "Now let's rewind, kind of the tape:"
rewind(current_file)

current_line = 1
# print "The current_line is %r." % current_line
print_a_line(current_line, current_file)

current_line = current_line + 1
# print "The current_line is %r." % current_line
print_a_line(current_line, current_file)

current_line = current_line + 1
# print "The current_line is %r." % current_line
print_a_line(current_line, current_file)

rewind_with_offset(current_file,12)
print current_file.readlines()

# -*- coding: utf-8-*-

from sys import argv

script, file_name = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(file_name)

print("First, let's print whole file: ")
print_all(current_file)

print("Now let's rewind, kind of the tape ")
rewind(current_file)

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line , current_file)

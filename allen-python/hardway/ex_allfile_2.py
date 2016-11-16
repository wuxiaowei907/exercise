# -*- coding: utf-8 -*-
import os

fo = open("test.txt", "wb")
print "Name of the file : ", fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
print "Softspace flag :", fo.softspace

fo.write("""xiaoming is a good student.
and xiaohua ,too.
""")

fo.close()

print "Close or not again : " , fo.closed

fo = open("test.txt", "a+")
print fo.tell()
fo.write("I'm so handsome.\n")
print fo.tell()
str = fo.read()
print "Reading string is : " , str
print fo.tell()
fo.write("Python is a good program dddlanguage.\n")
print fo.tell()
fo.seek(1)
print "all file content: ", fo.read()
fo.close()

print "Close or not agian: ", fo.closed

os.rename("foo.txt","test.txt")

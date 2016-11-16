# -*- coding : utf-8 -*-

from sys import argv
from os.path import exists

script, from_file, to_file = argv

# print("Coping file from %r to %r." % (from_file, to_file))
#
# in_file = open(from_file)
# indata = in_file.read()
#
# print("The input file have %d bytes data." % len(indata))
#
# print("Does the out file exits? %r" % exists(to_file))
# print("Ready? hit Return to continue or hit CTRL-C to abort.")
# input()
#
# out_file =  open(to_file,"w")
# out_file.write(indata)
#
# print("Alright, all done!")
#
# out_file.close()
# in_file.close()
print("The computer will copy %r to %r." % (from_file, to_file),
    "\nYou can hit Return to continue ,or quit by hitting CTRL-C.")
input("? ")

in_file = open(from_file)
out_file = open(to_file, 'w')

out_file.write(in_file.read())

print("All done.")

in_file.close()
out_file.close()

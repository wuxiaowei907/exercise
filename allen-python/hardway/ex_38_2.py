# -*- coding: utf-8 -*-

ten_thing = "Apples Oranges Crows Telephone Light Suger"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_thing.split(" ")

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d itmes now." % len(stuff)

print "Here we go: ", stuff

print stuff[1]
print stuff[-1]

print stuff[:4]

print stuff[2:4]

print stuff[1:-2]

print ",".join(stuff)
print "#".join(stuff[3:6])

print stuff

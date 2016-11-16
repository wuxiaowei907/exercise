# -*- coding: utf-8 -*-

the_count = [1, 2, 3, 4, 5]
fruits =  ["Apples", "Oranges", "Peers", "Apricots"]
changes = [1, "pennies", 2, "dimes", 3, "quarters"]

for count in the_count:
    print "This is count %d" % count

for fruit in fruits:
    print "A fruit of type : %s" % fruit

for change in changes:
    print "I got a %r." % change

elements = []

for i in range(0,6):
    print "add %d into the elements." % i
    elements.append(i)

for i in elements:
    print "Element was %d" % i

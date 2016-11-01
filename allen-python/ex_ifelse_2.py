# -*- coding: utf-8 -*-

people = 30
cars = 40
trucks = 13

if people < cars:
    print "We should take the cars."
elif people > cars:
    print "We should not take the cars."
else:
    print "We can't decide."

if trucks > cars:
    print "There are too many trucks."
elif trucks < cars:
    print "Maybe we should take the trucks."
else:
    print "We still cannot  decide."

if people > trucks:
    print "OK, Let's just take the trucks."
else:
    print "Let's stay home then."

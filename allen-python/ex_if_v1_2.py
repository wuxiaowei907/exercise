# -*- coding : utf-8 -*-

people = 20
cats = 30
dogs = 15

if people < cats:
    print "There are too many cats. The world is doomed."

if people > cats:
    print "Not too many cats. The world is saved."

if people < dogs:
    print "The world is drools on."

if people > dogs:
    print "The world is dry."

dogs += 5

if people <= dogs:
    print "People is less than or equal to dogs."

if people >= dogs:
    print "People is greater than or equal to dogs."

if people == dogs:
    print "People are dogs"

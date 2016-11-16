# -*- coding: utf-8 -*-

name = 'Allen Wu'
age = 29
height = 180 # cm
weight = 85 # kg
my_eye = 'Black'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about %s." % name
print "He's %d cm tall." % height
print "He's %d kg heavy." % weight
print "Actually that's too fat."
print "He's got %s eyes and %s hair." % (my_eye, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

print "print anything(str): %r " % 'xiaio'
print "print anything(int): %r " % age
print "print anything(float): % r" % 4.5
print "print anything(list): %r" % [1,2,3]
print "print anything(map): %r" % {"sd":23}

print "print round(%%d):%d" % round(3.5343)


# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight
)

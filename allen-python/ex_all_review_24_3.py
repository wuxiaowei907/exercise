# -*- coding: utf-8 -*-

print("Let's practice everything.")
print('You\'d need to know about escapes with \\ that do \n newlines and \t tabs.')

poem =  """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of lovely
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none
"""

print("--------------------")
print(poem)
print("--------------------")

five = 10 + 3 - 2 - 6
print("This should be five: %s" % five)

def secret_formula(started):
    jelly_beans = started * 500
    jar = jelly_beans / 1000
    crates = jar / 100
    return jelly_beans, jar, crates

start_point = 10000
jelly_beans, jar, crates = secret_formula(start_point)
print("With a start pointing of : %d" % start_point)
print("We'd have %d beans, %d jars and %d crates." % (jelly_beans, jar, crates))

start_point = start_point / 10
print("We can also do that this way:")
print("We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point))

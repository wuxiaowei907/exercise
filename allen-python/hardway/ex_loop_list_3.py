# -*- coding: utf-8 -*-

the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "peers", "apricots"]
changes = [1, "pennies", 2, "dimes", 3, "quarters"]

# the first kind of for-loop goes though a list
for number in the_count:
    print("This is count: %d." % number)

# same as above
for fruit in fruits:
    print("a fruit of type: %s." % fruit)

# also we can go throug mixed lists too
# notice we have to use %r since we do't know what's in it
for i in changes:
    print("I got %r." % i)

# we can also build lists, first start with an empty element
elements = []

#Then we use range function to do 0 to 5 counts
for i in range(0, 6):
    print("Adding %d to the list. " % i)
    # append is a function list can Understand
    elements.append(i)

# now we can print them too
for i in elements:
    print("This is a count: %d." % i)

elements2 = list(range(0,10,2))
print(elements2)

element3 = []

for i in range(1,stop=None,2):
    element3.append(i)
    if i >= 100:
        break

print(element3)

# -*- coding: utf-8 -*-

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    str_cheese = "" if cheese_count == 0 or cheese_count == 1 else "s"
    print("You have %d cheese%s!" % (cheese_count, "" if cheese_count == 0 or cheese_count == 1 else "s"))
    print("You have %d boxes of cracker%s!" % (boxes_of_crackers, "" if boxes_of_crackers == 0 or boxes_of_crackers == 1 else "s"))
    print("Man, That's enough for a party.")
    print("Get a blanket.\n")
    boxes_of_crackers = 10

print("We can just give the function numbers directly:")
cheese_and_crackers(1, 1)

print("OR,We can use variables from our script:")
amount_of_cheese = 30
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
print(amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 23, 34 + 23)

print("And we can combine the two, varibales and math:")
cheese_and_crackers(amount_of_cheese + 11, amount_of_crackers + 13)

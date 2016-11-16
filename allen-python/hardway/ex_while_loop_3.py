# -*- coding: utf-8 -*-

i = 0
number = []

end = input("input a end number for loop: ")
step = input("loop steps: ")
try:
    while i < int(end) :
        print("At the top, the i is %d." % i)
        number.append(i)

        i += int(step)
        print("Numbers now:", number)
        print("At the bottom, the i is %d." % i)

    print("Numbers contain:")

    for i in number:
        print(i)
except ValueError:
    print("Please input the number")

number.clear()
print("numbers after clear,", number)
try:
    for i in range(0,int(end),int(step)):
        number.append(i)

    print("numbers:", number)
except ValueError as e:
    print(e.message)

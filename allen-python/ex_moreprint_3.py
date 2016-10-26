# -*- coding: utf-8 -*-

print("Mary had a little lamb.")
print("Its fleece was white as %s." % 'snow')
print("And everything that mary went.")
print("." * 10) # duplicate . ten times

l =  list([1,2,3] * 2)
print(l)
t = tuple(l * 2)
print(t)

m = {"key":12,"value":9}
#print(m * 2) that can't run,unsupported operand type(s) for *: 'dict' and 'int'
s = set(["a","b"])
print(s)
# print(s * 10) that alse cannot run,unsupported operand type(s) for *: 'set' and 'int'

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1 + end2 + end3 * 10 + end4 + end5 + end6,) # commas making the print  don't chengel line
print(end7 + end8 + end9 + end10 + end11 + end12)

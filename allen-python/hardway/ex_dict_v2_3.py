# -*- coding: utf-8 -*-

def func(**argv):
    type(argv)
    for key, value in argv.items():
        print(key," = ", value)

func(step=1,ordd = "2")

dicts = {"name": "allen", "age": "12", "score" : 100}

dicts_copy = dicts.copy()

print(dicts)
print(dicts_copy)

dicts_copy.clear()
print(dicts_copy)

dicts_copy = dicts.copy()

keyname = ["name", "age1"]

dicts_copy2 = dicts.fromkeys(keyname,"kkk") #不明白
print(dicts)
print(dicts_copy2)

def func1(*param):
    print(param)
    for i in param:
        print(i)
func1(1,2,'ddd',(1,"d"))

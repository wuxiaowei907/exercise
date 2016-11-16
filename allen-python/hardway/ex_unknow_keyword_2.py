# -*- coding: utf-8 -*-

from sys import argv
# print argv[1]
# # and as assert
# assert argv[1] == "11", "assert error"
#
# # break
#
# for i in range(1,5):
#     for j in range(100,500,100):
#         if j > 300:
#             break
#         else:
#             print (i,j)
# # class
#
# class Person(object):
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def add(self, score):
#         self.score = score
#
#     def __str__(self):
#         return "name: %s, age: %d, score: %d" % (self.name, self.age, self.score)
#
# person = Person("allen",28)
# person.add(100)
# print person
# del person.score
# # print person
#
# #continue def del
# otherperson = {"name":"Kavin", "age": 3, "score": 100}
# print otherperson
# del otherperson["score"]
# print otherperson
#
# # elif else except
#
# a = raw_input("kkk> ")
#
# try:
#     print int(a), person
#
# except ValueError as e:
#
#     print e.message
# except AttributeError as e2:
#
#     print e2.message
# else:
#     print "unknow error"
#
# command  = raw_input("input some python command: ")
# exec command

#finally for from global

name = "Amad"
print name
def fun1():
    name = "xim"
fun1()
print name
def fun2():
    global name
    name = 'lal'
fun2()
print name

# if import in

x = 20

if x in range(11,22):
    print "lsdk"

# is just judge two variable is one object

# lambda

s= lambda x : x ** x
print(s(3))

#not or pass print raise  return try while with yield

y
print y==None

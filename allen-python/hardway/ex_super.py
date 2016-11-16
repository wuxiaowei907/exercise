# -*- coding: utf-8 -*-
class Base(object):
    def __init__(self):
        print "Base created"

class ChildA(Base):
    def __init__(self):
        Base.__init__(self)

class ChildB(Base):
    def __init__(self):
        super(ChildB, self).__init__()

print ChildA(),ChildB()

# 新式类
class A(object):
    def __init__(self):
        print 'A'

class B(A):
    def __init__(self):
        super(B, self).__init__()
        print 'B'

class C(B, A):
    def __init__(self):
        super(C, self).__init__()
        print 'C'

print C()

class Person(object):
    name = ""
    sex = ""
    def __init__(self, name, sex='U'):
        print 'Person'
        self.name=name
        self.sex=sex


class Consumer(object):
    def __init__(self):
        print 'Consumer'

class Student(Person, Consumer):
    def __init__(self, score,name):
        print Student.__bases__
        super(Student, self).__init__(name, sex='F')
        Consumer.__init__(self)
        self.score=score

s1 = Student(90, 'abc')
print s1.name, s1.score, s1.sex

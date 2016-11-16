# -*- coding: utf-8 -*-

class Bar(object):

    def func1(self,name):
        print name

class Foo(Bar):

    # def func1(self,name):
    #     print "hello,", name

    def func2(self, age):
        super(Foo,self).func1(age)
        print "Allen,",age

foo = Foo()
foo.func1("allen")
foo.func2("29")

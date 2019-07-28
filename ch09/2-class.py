# !user/bin/python
# -*- coding: UTF-8 -*-

class Dog:
    lst = []
    def __init__(self, name):
        self.name = name
    def func(self):
        print('Love me, love my dog')

d1 = Dog('xiaoming')
d2 = Dog('xiaoming')
d1.lst.append('nihao')
d2.lst.append('wobuhao')
print(Dog.lst) # 这里的Dog是类变量，所有的对象共享这个变量，为了避免这个，应该用下面的方法

# 避免使用类变量
class Cat:
    def __init__(self, name):
        self.name = name
        self.lst = []
    def func(self):
        print('Love me, love my cat')
d1 = Cat('xiaoming')
d2 = Cat('xiaoming')
d1.lst.append('nihao')
d2.lst.append('wobuhao')
print(d1.lst)
print(d2.lst)

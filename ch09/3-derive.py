# !user/bin/python
# -*- coding: UTF-8 -*-

class Dog:
    def __init__(self, name):
        self.name = name
    def cry(self, barking):
        print(barking)

class Puppy(Dog):
    def __init__(self, name, age): # 重写构造方法，添加了一个姓名
        super().__init__(name) # 这里不用加self
        self.age = age
    def cry(self, barking): # 重写cry方法
        super().cry(barking) # 这里不用加self
        print(barking * 2, self.age)

pp = Puppy('xiaoming', 21)
pp.cry('wangwangwang')
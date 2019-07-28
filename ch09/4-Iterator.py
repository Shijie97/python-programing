# !user/bin/python
# -*- coding: UTF-8 -*-

s = 'abc'
it = iter(s)
try:
    while True:
        print(next(it))
except StopIteration:
    print("over")

# 迭代器用于class中
class A:
    def __init__(self, data):
        self.data = data
        self.index = -1
    def __iter__(self): # 如果next方法已经定义，直接返回self
        return self
    def __next__(self):
        if self.index == len(self.data) - 1: # 这里终止的条件是len - 1
            raise StopIteration # 如果终止就停止迭代
        else:
            self.index = self.index + 1
            return self.data[self.index]

a = A([1, 2, 5, 7, 9])
for i in a:
    print(i)

def B(data):
    for x in data[:]:
        yield x ** 2

b = B([1, 2, 5])
for i in b:
    print(i)

# https://www.jianshu.com/p/9dd355ab4e5d
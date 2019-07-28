# !user/bin/python
# -*- coding: UTF-8 -*-
for i in range(0, 10):
    print(i)
print("--------------")
for i in range(0, 10, 4):
    print(i)
words = ['cat', 'dog', 'cow']
for i, w in enumerate(words):
    print(i, w)
print(range(10))# 返回的不是一个列表而是一个对象，成为可迭代的对象，常见的迭代器有for循环和list()函数
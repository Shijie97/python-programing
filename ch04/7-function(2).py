# !user/bin/python
# -*- coding: UTF-8 -*-
def fib2(n):
    """定义一个斐波那契数列，不打印，返回一个list"""
    lst = []
    a, b = 1, 1
    while(a <= n):
        lst.append(a)
        a, b = b, a + b
    return lst

f = fib2(100)
print(f) # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(type(f)) # <class 'list'>
print (1 in f) # True
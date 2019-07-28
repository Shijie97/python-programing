# !user/bin/python
# -*- coding: UTF-8 -*-
# 返回一个n以内的斐波那契数列，这方法也太巧妙了吧
def fib(n):
    a, b = 1, 1
    while(a <= n):
        print(a, end = ' ') # 不换行，用空格代替换行符
        a, b = b, a + b
print(fib(0)) # None，什么也不return
f = fib(20) # 调用的同时赋值给f, fib(20)返回值为None
print(f) # None
ff = fib # 这才是赋值
ff(10)
print(ff(10)) # None，无return

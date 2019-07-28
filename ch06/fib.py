# !user/bin/python
# -*- coding: UTF-8 -*-

def fib1(n):
    a, b = 1, 2
    res = []
    i = 0
    while a < n:
        res.append(a)
        a, b = b, a + b
    return res


def fib2(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib2(n - 1) + fib2(n - 2)




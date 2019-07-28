# !user/bin/python
# -*- coding: UTF-8 -*-
def func(a, b = 2, c = "hello"): # 默认参数一定是从最后一个开始往左连续存在的
    print(a, b, c)

func(2, 100) # 覆盖了b = 2

i =5
def f(arg = i):
    print(i)
i = 6
f() # 6

# 在一段程序中，默认值只被赋值一次，如果参数中存在可变数据结构，会进行迭代
def ff(a, L = []):
    L.append(a)
    return L

print(ff(1)) # [1]
print(ff(2)) # [1, 2]
print(ff(3)) # [1, 2 ,3]

# 不想迭代的话，就如下所示
def fff(a, L = None):
    if L is None:
        L = []
    L.append(a)
    return L

print(fff(1)) # [1]
print(fff(2)) # [2]
print(fff(3)) # [3]

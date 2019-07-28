# !user/bin/python
# -*- coding: UTF-8 -*-

# 传入元组和字典，只不过*传入的是元组，**传入字典，元组必须在字典前面
# *表示任何多个无名参数，本质为元组
# **表示关键字参数，本质为字典
def func(*tup, **dict):
    for t in tup:
        print(t)
    print('*' * 40)
    keys = sorted(dict.keys())
    for k in keys:
        print("key:", k, "value:", dict[k])

func(1, 2, 3, x = 1, y = 2) # 这里x不用打单引号，但是在数组定义的时候要打

# 参数列表的解引用
tup = (10, 11, 20)
dict = {'x' : 10, 'y' : 20, 'z' : 30}

func(*tup, **dict)

def concat(sep, *args):
    return sep.join(args)

print(concat('/', 'a', 'b', 'c')) # a/b/c
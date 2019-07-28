# !user/bin/python
# -*- coding: UTF-8 -*-

# lambda表达式有点像匿名函数

list = [-6, 100, -72, 0, 66, 2]
# 对list按绝对值升序排序
new_list = sorted(list, key = lambda x : abs(x))
print(new_list)

def make_increcement(n):
    return lambda x : x + n

f = make_increcement(42)
print(f(0)) # 42
print(f(1)) # 43

dict = [(4, 'four'), (2, 'two'), (0, 'zero'), (8, 'eight')]
new_dict = sorted(dict, key = lambda x : x[1]) # x指的是列表里每一个元素，按第二个元素升序，即字母
print(new_dict)
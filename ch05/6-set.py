# !user/bin/python
# -*- coding: UTF-8 -*-

s = {1, 2, 4, 5, 8}
print(type(s)) # <class 'set'>
print(s)
print(len(s))

# 创造空集合只能用set()
s = set()
print(type(s)) # <class 'set'>
print(s) # set()

# 去重
lst = [1, 1, 2, 2, 5]
print(list(set(lst)))

# 构建
s = set('abcdefg')
print(s) # {'a', 'c', 'e', 'g', 'd', 'f', 'b'}

# 列表推导式
res = {x for x in s if x not in {'a', 'b', 'c'}}
print(res)
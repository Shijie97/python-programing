# !user/bin/python
# -*- coding: UTF-8 -*-

lst = list(range(10))
print(lst)
del lst[6 : -1] # 6, 7, 8不见了
print(lst)
del lst[:]
print(lst)
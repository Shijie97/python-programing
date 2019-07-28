# !user/bin/python
# -*- coding: UTF-8 -*-
import copy

# deepcopy，方法一copy.deepcopy
lst1 = [1, 2, 3]
lst2 = copy.deepcopy(lst1)
print(lst2)
print(lst1 == lst2) # True，仅判断值是否相等
print(lst1 is lst2) # False，地址不同啦

# deepcopy，方法二[:]
lst3 = lst1[:]
print(lst3 is lst1) # False

# deepcopy，方法三list()
lst3 = list(lst1)
print(lst3 is lst1) # False

# deepcopy，方法四lst.copy
lst3 = lst1.copy() # 这里是list自带的copy，默认为deepcopy
print(lst3 is lst1) # False

# shallowcopy
lst3 = lst1
print(lst3 is lst1) # True
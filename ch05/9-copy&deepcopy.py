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
lst3[0] = 100

# deepcopy，方法三list()
lst3 = list(lst1)
print(lst3 is lst1) # False

# deepcopy，方法四lst.copy
lst3 = lst1.copy() # 这里是list自带的copy，默认为deepcopy
print(lst3 is lst1) # False

# deepcopy，方法五 Numpy库中的ndarray.copy()
a = np.arange(10)
b = a.copy()
print(a is b) # False
b[0] = 100
print(a) # [0 1 2 3 4 5 6 7 8 9]
print(b) # [100   1   2   3   4   5   6   7   8   9]

# shallowcopy，直接赋值
lst3 = lst1
print(lst3 is lst1) # True

# shallowcopy，Numpy库中的切片或者View函数
# 浅拷贝：调用view函数 / 切片
# view函数或者切片，区别于直接赋值，因为地址会改变，但是内容仍指向原来的内容
a = np.arange(10)
b = a.view()
print(id(a) == id(b)) # False
print(a is b) # False
b[0] = 100
print(a) # [100   1   2   3   4   5   6   7   8   9]
print(b) # [100   1   2   3   4   5   6   7   8   9]

# 浅拷贝：切片
# 会更改原来的值，但是地址不同，等同于view
print('*' * 50)
a = np.arange(10)
b = a[:]
c = a[1:]
b[0] = 101
c[0] = 102
print(a) # [101 102   2   3   4   5   6   7   8   9]
print(b) # [101 102   2   3   4   5   6   7   8   9]
print(c) # [102   2   3   4   5   6   7   8   9]
print(id(a), id(b), id(c)) # 2355930764512 2355930764592 2355913162544
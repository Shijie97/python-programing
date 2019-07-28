# !user/bin/python
# -*- coding: UTF-8 -*-

import math

# str和repr区别
# str输出的是给人看的，而repr是给机器看的，因此要在外面多一层引号
print(str("hello,world!")) # hello, world
print(repr("hello,world!")) # 'hello, world'
print(str(1000))
print(repr(1000))
print(str((1, 2, 'a')))
print(repr((1, 2, 'a')))

# 打印立方表
# 方法一
for x in range(1, 11):
    print(str(x).rjust(2), str(x ** 2).rjust(3), end = ' ')
    print(str(x * x * x).rjust(4))

# 方法二，用format，注意format里面的{}之间不需要逗号，且冒号两边不能空格，math.pow记得显式转换
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, int(math.pow(x, 2)), int(math.pow(x, 3))))

# format方法 https://www.jianshu.com/p/4d496f49f824

s = '{aa} is {bb}'.format(bb = 5, aa = 'hahaha')
print(s) # hahaha is 5
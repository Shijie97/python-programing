# !user/bin/python
# -*- coding: UTF-8 -*-

# 字典遍历
dic = {x : x ** 2 for x in range(10)}
for k, v in dic.items():
    print(k, v)

# 数组遍历
lst = list(range(10))
for i, e in enumerate(lst):
    print(i, e)

# zip打包
lst1 = [chr(x) for x in range(97, 97 + 26)]
lst2 = list(range(97, 97 + 26))
for c, n in zip(lst1, lst2):
    print('{0} -> {1}'.format(c, n))
print(list(zip(lst1, lst2))) # 元组对儿，一溜儿存在一个list里面

# 如果循环的时候想要修改正在遍历的序列，则应该遍历其副本
lst = list(range(10))
for e in lst[:]: # 这里用的就是副本
    if e > 5:
        lst.remove(e)
print(lst)
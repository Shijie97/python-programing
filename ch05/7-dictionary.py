# !user/bin/python
# -*- coding: UTF-8 -*-

dic = {'x' : 1, 'y' : 2}
dic['z'] = 3
print(dic)
print(list(dic.keys())) # 返回key组成的数组，无序
print(sorted(list(dic.keys()))) # sorted返回值
print('z' in dic) # True

# 创建方式
dic = dict([('a', 5), ('b', 7)]) # 相当于调用了dict的构造函数
print(dic)

dic = {x : x ** 2 for x in range(10)}
print(dic)

dic = dict(a = 4, b = 6)
print(dic) # {'a': 4, 'b': 6}

# get方法
print(dic.get('a', 0)) # 4 返回key 'a' 对应的value，如果没有返回默认值0
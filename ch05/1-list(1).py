# !user/bin/python
# -*- coding: UTF-8 -*-

lst = [0, 1, 2, 3, 2]
lst.append(5)
print(lst) # [0, 1, 2, 3, 4, 5]
lst2 = [100, 101]
lst.append(lst2) # [0, 1, 2, 3, 4, 5, [100, 101]] lst作为整体接入
print(lst)
lst.extend(lst2) # [0, 1, 2, 3, 4, 5, [100, 101], 100, 101], 元素单独接入
print(lst)
res = lst.insert(0, -1)
print('lst insert', lst)
res = lst.remove(2) # 移除第一个值为2的元素，这里2不代表index
print('res remove', res)
print('lst remove', lst)
res = lst.pop() # pop返回最后一个，并退栈
print('res pop', res)
print('lst pop', lst)
res = lst.index([100, 101]) # 返回第一个值为[100, 101]的index
print('res index', res)
print('lst index', lst)
print(lst.count(100)) # 返回100出现的次数
print(len(lst))
lst.reverse() # reverse不返回值，直接逆置
print(lst)
del lst[1]
print(lst)
lst.sort() # sort不返回值，直接排序
print(lst)
lst.clear() # 置空
print('lst clear', lst)
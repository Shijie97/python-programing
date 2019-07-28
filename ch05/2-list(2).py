# !user/bin/python
# -*- coding: UTF-8 -*-
from collections import deque

lst = [100, 1, 2, 3, 2]

# 列表当做stack使用
lst.append(5) # push
print(lst)
lst.pop() # pop
print(lst)

# 列表当做queue用
queue = deque(lst)
print(queue)
queue.append(5) # 入队 deque([0, 1, 2, 3, 2])
print(type(queue)) # <class 'collections.deque'>
print(queue)
res = queue.popleft() # 出队，并返回出队的元素
print(res)
print(queue)
print(list(queue)) # 强制转化成list结构
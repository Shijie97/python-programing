# !user/bin/python
# -*- coding: UTF-8 -*-

# 列表推导式，map映射
res = map(lambda x : x ** 2, range(0, 10))
print(type(res)) # <class 'map'>
print(type(range(0, 10))) # <class 'range'>
print(res) # <map object at 0x0000028D895C63C8>，是一个对象
print(range(0, 10)) # range(0, 10)
print(list(res))

# 上述做法也可以用下面的写法来完成
res = [x ** 2 for x in range(0, 10)]
print(res)
res = list(x ** 2 for x in range(0, 10))
print(res)

# for和if可以一起使用
res = [(x, y) for x in (1, 2, 3) for y in (1, 2, 6) if x != y]
print(res) # [(1, 2), (1, 6), (2, 1), (2, 6), (3, 1), (3, 2), (3, 6)]
res2 = [(x, y) for (x, y) in res if x > y] # 找出x大于y的
print(res2)

# 矩阵转置，利用zip(*)解压，而zip()表示压缩，zip之后要强转成list形式
res = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
res2 = list(zip(*res))
print(res2)
print(list(zip(res[0],res[1]))) # zip()表示压缩
print(list(zip(*list(zip(res[0],res[1]))))) # # zip(*)表示解压

# 或者也可以用一下方式完成矩阵转置，传统方法
new_res = []
for i in range(len(res[0])):
    t = []
    for j in range(len(res)):
        t.append(res[j][i])
    new_res.append(t)
print(new_res)

# for in的另一个例子
lst = [[1, 2], [3, 4], [5, 6]]
new_lst = [e[0] for e in lst] # 取每个元素第一个
print(new_lst)
new_lst = list(map(lambda x : x[0], lst)) # 取每个元素第一个
print(new_lst)

# 看懂了上面这个例子，我们可以用一行解决矩阵转置问题，当然，zip函数就可以一行
new_res = [[e[i] for e in res] for i in range(len(res[0]))]
print(new_res)
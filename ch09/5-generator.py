# !user/bin/python
# -*- coding: UTF-8 -*-

def f():
    print('start...')
    a = yield 5
    print('a = ', a)
    b = yield 6
    print('b = ', b) # 永远不会被执行

ob = f() # 带有yield的函数就是一个生成器
res1 = next(ob) # 首次运行生成器不能传参，因为还没碰到yield，这里将执行第一个yield之前的程序，并且将yield的返回值传给res1，函数里面的a，因为没有传参进来，所以目前是None
print('res1:', res1) # 此时res1为5，程序此时停留在'a = yield 5'这一行，因为next遇到yield跳出来了
res2 = ob.send('msg') # 第二次运行生成器，此时停留在'a = yield 5'这一行，因此，a从None变成'msg'，并且继续执行代码直至遇到下一个yield并停留在yield那一行然后退出
print('res2:', res2) # 此时res2返回6，然后跳出函数，b这个时候为None，可惜永远都输出不了了


# start...
# res1: 5
# a =  msg
# res2: 6

new_ob = f()
for i in new_ob:
    print(i)

# start...
# 5
# a =  None
# 6
# b =  None



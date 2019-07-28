# !user/bin/python
# -*- coding: UTF-8 -*-

# 给异常传递参数
try:
    raise Exception('hahaha', 'hiahiahia')
except Exception as ex:
    print(type(ex)) # <class 'Exception'>
    print(type(ex.args)) # <class 'tuple'>，哪怕传入参数只有一个也是元组
    print(ex.args[0]) # hahaha

# 抛出异常，用raise
# 在except语句中执行raise，就相当于重新执行了该异常
try:
    raise NameError('Jay')
except NameError as ex:
    print('An error came up named', str(ex.args[0]))
    raise # 重新抛出异常
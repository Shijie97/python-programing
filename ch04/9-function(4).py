# !user/bin/python
# -*- coding: UTF-8 -*-
# 函数以及函数调用的关键字参数

def dog(eyes, name = "wangcai", nationality = "CN"):
    print("eyes:", eyes, "name:", name, "nationality:", nationality)

#调用的时候，如果全不指定参数，则顺着来，只要指定一个，剩下的默认参数必须也指定
dog(10)
dog(eyes = 10)
dog(eyes = 10, name = "xiaoming")
dog(name = "xiaoming", eyes = 10)
dog(10, "xiaoming") # 对应前两个
dog("xiaoming", 10) # 也对应前两个
dog(10, nationality = "xiaoming")
#dog(eyes = 10, "xiaoming") # error，"xiaoming"必须指定参数名
#dog(nationality = "xiaoming", 10) # error
#dog(name = "xiaoming", 10) # error
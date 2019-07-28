# !user/bin/python
# -*- coding: UTF-8 -*-

# python引用变量的顺序： 当前作用域局部变量>外层作用域变量>当前模块中的全局变量>python内置变量
# nonlocal，指定的变量为外层作用域中的非全局变量
def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"
    spam = "test spam"
    # 下面的三个print，要打印的spam，其实都是scope_test作用域中的spam
    do_local()
    print("After local assignment:", spam) # 这个函数没有改变scope_test作用域中的spam
    do_nonlocal()
    print("After nonlocal assignment:", spam) # 这个函数用了nonlocal，改的就是scope_test作用域中的spam
    do_global()
    print("After global assignment:", spam) # 这个函数定义了一个全局变量spam，这个全局变量spam并不是scope_test作用域中的spam，因此和上面那个函数保持一致

scope_test()
print("In global scope:", spam) # 这里要输出的spam，就是全局的spam了，因为scope_test的生命周期已经结束啦

# After local assignment: test spam
# After nonlocal assignment: nonlocal spam
# After global assignment: nonlocal spam
# In global scope: global spam
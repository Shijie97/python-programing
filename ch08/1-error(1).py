# !user/bin/python
# -*- coding: UTF-8 -*-

while True:
    try:
        x = int(input('enter a number:'))
        # break
    except ValueError:
        print('Error! Try Again!')
    except RuntimeError:
        print('RuntimeError!')
    except:
        print('Other Error') # 通配符，不提倡这样使用
    else:
        print('No Error!') # 在所有except后面加上else，表示没有发生错误后应该干的事
# !user/bin/python
# -*- coding: UTF-8 -*-

# write 如果没有就新建，如果有就覆盖\
# r 可读，默认为这个
# w 写入，没有则新建，有则覆盖
# a 追加，自动加到最有一行末尾
# r+ 文件读取和写入

# f = open('test.txt', 'r+')
# f.write('helo')
# print(f.read())
# print(f.tell())
# f.close()

f = open('test.txt', 'a')
f.write('\n')
f.write('wuwuwu')
f.close()

f = open('test.txt', 'r')
# print(f.readlines()) # readlines将所有行读取到一个list里面
for line in f: # 逐行输出
    print(line, end = '') # 这里''里面什么也没有，因为f每一行最后自带换行，因此不必print再换行了
f.close()

# 推荐使用with用法，这种方法不用close
with open('test.txt', 'r') as f:
    print(f.read())
    print('*' * 18)

# !user/bin/python
# -*- coding: UTF-8 -*-
import math
for i in range(2, 51):
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j ==0 and i // j != 1:
            print(i, "=", j, "*", i // j)
            break
    else: #for循环的else语句在break未执行的情况下运行，若无break，照常运行
        print(i, "is a prime")

for i in range(1, 11):
    if i % 2 == 0:
        print(i, "is a even number")
    else:
        print(i, "isn't a even number")
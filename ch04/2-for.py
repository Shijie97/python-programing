#!user/bin/python
# -*- coding: UTF-8 -*-
words = ['cat', 'dogdog', 'mouse']
for w in words:
    print(w, len(w))

for w in words[:]: # 这里不能用words只能用words[:]，因为word[:]是复制的切片，如果用words就会陷入死循环
    if len(w) >= 5:
        words.insert(0, w)
print(words)
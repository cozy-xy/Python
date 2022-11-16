# 迭代（遍历）
d = {'a':1,'b':2,'c':3}
# dict 默认迭代的是key
for key in d:
    print(key)

# a
# b
# c
# dict存储不是按list顺序排列的，其结果也不会相同

# dict 迭代value
for value in d.values():
    print(value)

# 1
# 2
# 3

# dict 同时迭代 key & value
for k,v in d.items():
    print(k,v)

# a 1
# b 2
# c 3

# 判断一个对象是可迭代对象？
from collections.abc import Iterable

print(isinstance('abc',Iterable))  # str是否可迭代  True
print(isinstance([1,2,3],Iterable)) # list是否可迭代 True
print(isinstance(123,Iterable)) # 整数是否可迭代 False

# list如何实现类似Java的下标循环？
# Python内置的enumerate函数可以把一个list变成索引-元素对
for i,value in enumerate(['A','B','C']):
    print(i,value)

# 0 A
# 1 B
# 2 C


for x,y in [(1,1),(2,4),(3,9)]:
    print(x,y)

# 1 1
# 2 4
# 3 9




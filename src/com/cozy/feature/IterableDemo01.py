# 迭代器：Iterator 可迭代对象：Iterable
# 判断一个对象是否是Iterable对象
from collections.abc import Iterable
print(isinstance([],Iterable)) # True
print(isinstance({},Iterable)) # True
print(isinstance('abc',Iterable)) # True
print(isinstance((x for x in range(10)),Iterable)) # True
print(isinstance(100,Iterable)) # False

# 判断一个对象是否是Iterator对象
from collections.abc import Iterator
print(isinstance((x for x in range(10)),Iterator)) # True
print(isinstance([],Iterator)) # False
print(isinstance({},Iterator)) # False
print(isinstance('abc',Iterator)) # False

# list、dict、str虽然是Iterable，却不是Iterator
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数
print(isinstance(iter([]),Iterator)) # True
print(isinstance(iter('abc'),Iterator)) # True



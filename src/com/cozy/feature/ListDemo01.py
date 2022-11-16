# 列表生成器
print(list(range(1,11)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 生成[1x1, 2x2, 3x3, ..., 10x10]
# 方法一（循环）
L = []
for x in range(1,11):
    L.append(x * x)
print(L)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 方法二（列表生成式）
print([x * x for x in range(1,11)])
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
print([x * x for x in range(1,11) if x % 2 == 0])
# [4, 16, 36, 64, 100]

# 可以使用两层循环，可以生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])
# ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

# 运用列表生成式，列出当前目录下的所有文件和目录名
import os # 导入os模块
print([d for d in os.listdir('.')]) # os.listdir可以列出文件和目录
# ['IterationDemo01.py', 'ListDemo01.py', 'SliceDemo01.py']

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k,v in d.items():
    print(k, '=', v)
# x = A
# y = B
# z = C

# 列表生成式可使用两个变量生成list
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k,v in d.items()])
# ['x=A', 'y=B', 'z=C']

# 将一个list中的所有字符变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])
# ['hello', 'world', 'ibm', 'apple']

# for后面的if是过滤条件，不能有else
print([x for x in range(1, 11) if x % 2 == 0])
# [2, 4, 6, 8, 10]
# for前面的if-else是表达式
print([x if x % 2 == 0 else -x for x in range(1, 11)])
# [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]


# 如果list中既包含字符串，又包含整数，将其所有字符变为小写
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str) == True]
print(L2) # ['hello', 'world', 'apple']
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
# 测试通过!























# 偏函数

# int函数：字符串转换为整数，十进制
print(int('12345'))

# int函数：提供额外 base 参数，默认值为10，N进制转换
print(int('12345',base=8))
print(int('12345',16))

# 转换大量的二进制字符串：定义一个int2函数，默认把 base=2 传进去
def int2(x,base=2):
    return int(x,base)

print(int2('1000000'))
print(int2('1010101'))

# functools.partial 可以创建一个int2函数
import functools
int2 = functools.partial(int, base=2)

print(int2('1000000'))
print(int2('1010101'))

# 新的int2函数，仅仅是把base参数重新设定默认值为2，但也可以在函数调用时传入其他值
print('1000000', base=10)

# 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
# 1、当传入：
int2 = functools.partial(int, base=2)
# 固定了int()函数的关键字base，也就是：
int('10010')
# 相当于
kw = {'base':2}
int('10010', **kw)

# 2、当传入：
max2 = functools.partial(max, 10)
# 实际上会把 10 作为 *args 的一部分自动加到左边，也就是：
max2(5, 6, 7)
# 相当于
args = (10, 5, 6, 7)
max(*args)
# 结果为 10


































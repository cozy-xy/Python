# 匿名函数
print(list(map(lambda x: x * x,[1,2,3,4,5,6,7,8,9]))) # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# lambda x: x * x
# def f(x):
#     return x * x

# lambda关键字表示匿名函数，冒号前面的 x 表示函数参数
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
# 1、匿名函数也是一个函数对象，可以把匿名函数赋值给一个变量，再利用变量来调用该函数
f = lambda x: x * x
print(f) # <function <lambda> at 0x000001A08A7DEAF0>
print(f(5)) # 25

# 2、可将匿名函数作为返回值返回
def build(x,y):
    return lambda: x * x + y * y

# 练习：用匿名函数改造下列代码
def is_odd(n):
    return n % 2 == 1

L1 = list(filter(is_odd, range(1, 20)))
L2 = list(filter(lambda n: n % 2 ==1 , range(1, 20)))
print(L1)
print(L2)





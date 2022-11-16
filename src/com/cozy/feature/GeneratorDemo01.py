# 列表生成式 & 生成器
L = [x * x for x in range(10)] # 列表生成式
print(L) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
g = (x * x for x in range(10)) # 生成器
print(g) # <generator object <genexpr> at 0x1022ef630>

# generator保存的是算法，是一边循环一边计算的机制
# 打印出generator的每一个元素
# 方法一：通过next()函数获得generator的下一个返回值
g = (x * x for x in range(10))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# 方法二：使用for循环，generator是可迭代对象
g = (x * x for x in range(10))
for n in g:
    print(n)

# 斐波那契数列（Fibonacci） 1,1,2,3,5,8,13,21,34...
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n = n + 1
    return 'done'

# 将fib函数变为generator
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n = n + 1
    return 'done'

# generator和函数的执行流程不一样。
# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

# 定义一个generator，依次返回数字1,3,5
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5
# 调用该generator时，首先要生成一个generator对象，然后用next()函数不断获得下一个返回值：
o = odd()
next(o)
next(o)
next(o)
next(o)

# 函数改成generator后，我们基本上从来不会用next()来获取下一个返回值，而是直接使用for循环来迭代
for n in fib(6):
    print(n) # 但缺少return返回值：done
# 1
# 2
# 3
# 5
# 8

# 用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

# 练习：杨辉三角：把每一行看做一个list，试写一个generator，不断输出下一行的list
def triangles():
    pass




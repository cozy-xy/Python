# 装饰器 Decorator

def now():
    print('2015-3-25')

# 函数也隶属于对象，函数对象可以被赋值给变量，因此，通过变量可以调用该函数
f = now
print(f())

# 函数对象有一个__name__属性，可以拿到函数的名字
print(now.__name__)
print(f.__name__)

# 装饰器：在函数调用前后自动打印日志，但又不修改now()函数的定义，在代码运行期间动态增加功能的方式，称之为“装饰器”
# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：
def log(func):
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 该log，是一个decorator，接受一个函数作为参数，并返回一个函数
@log   # 借助Python @ 语法
def now():
    print('2015-3-25')
# 调用now函数，会运行now函数本身，在其之前会打印一行日志
print(now()) # 执行 now = log(now)
# 结果：
# call now():
# 2015-3-25

# ===========================================================
# 自定义log文本
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

# 首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。

@log('execute')
def now():
    print('2015-3-25')

print(now()) # 执行 now = log('execute')(now)
# 结果：
# execute now():
# 2015-3-25

# 问题：过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：
# 因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，
# 否则，有些依赖函数签名的代码执行就会出错。
# 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

# 练习：请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import time, functools

def metric(fn):
    print('%s executed in %s ms' % (fn.__name__, 10.24))
    return fn

# 待续，未写完

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')





















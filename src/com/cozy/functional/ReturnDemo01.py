# 返回函数

# 求和函数
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

# 返回求和函数
# 返回函数在其内部引用了局部变量args
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

# 函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。


# 当调用 lazy_sum函数时，每次调用都会返回一个新的函数，即使传入相同的参数
f1 = lazy_sum(1,3,5,7,9)
f2 = lazy_sum(1,3,5,7,9)
print(f1 == f2) # False
# f1()与f2()的调用结果互不影响

# ===================================================================

# 闭包

# 当一个函数返回一个函数后，其内部的局部变量还会被新函数引用
# 返回的函数并未立刻执行，知道调用到f()才执行

def count():
    fs = []
    for i in range(1,4): # 在每次循环中，都创建了一个新函数，然后把创建的3个函数都返回了
        def f():
            return i*i
        fs.append(f)
    return fs

f1,f2,f3 = count()
# 其结果均为9 ，原因在于返回的函数引用了变量i，但他并非立即执行，等到3个函数都返回时，他们所引用的变量i已经变成了3，因此最终结果均为9

### 【重点】返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

# 如何改进呢，
# 方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))# f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
# 其结果为1,4,9

# 练习：
# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    fs = [0]
    def counter():
        fs.append(fs[-1] + 1)
        return fs[-1]
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')



























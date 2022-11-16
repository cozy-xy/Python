# 参数组合
# 参数定义顺序：必选参数、默认参数、可变参数、命名关键字参数、关键字参数
def f1(a,b,c = 0,*args,**kw):
    print('a =', a,'b =', b,'c =', c,'args =', args,'kw =', kw)

def f2(a,b,c = 0,*,d,**kw):
    print('a =', a,'b =', b,'c =', c,'d =', d,'kw =', kw)

print(f1(1,2))
# a = 1 b = 2 c = 0 args = () kw = {}
# None
print(f1(1,2,c = 3))
# a = 1 b = 2 c = 3 args = () kw = {}
# None
print(f1(1,2,3,'a','b'))
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
# None
print(f1(1, 2, 3, 'a', 'b', x=99))
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
# None
print(f2(1, 2, d=99, ext=None))
# a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
# None

# 通过一个tuple和dict，也可调用上述函数
args = (1,2,3,4)
kw = {'d': 99, 'x': '#'}
print(f1(*args, **kw))
# a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
# None

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
print(f2(*args, **kw))
# a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
# None


# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def mul(x,y):
     return x * y

# 修改
def mul(x,*y):
    print(x,y)
    for i in y:
        x = x * i
    return x

print(mul(1,2,3,4))
# 1 (2, 3, 4)
# 24






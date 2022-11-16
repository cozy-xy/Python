# __slots__
# __len__():让class作用于len()函数

# 1、__str__
class Student(object):
    def __init__(self, name):
        self.name = name

print(Student('Michael'))
# <__main__.Student object at 0x000002C71EB848B0> --
# 这是一个Student的实例，后面一段数字是内存地址，每个object的地址都不一样

# 使用__str__可以返回一个字符串
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

print(Student('Michael')) # Student object (name: Michael)

# 若将一个变量指向一个Student的实例
s = Student('Michael')
# 在命令行直接输入s时，返回的值仍是一个地址
# >>> s
# <__main__.Student object at 0x109afb310>
# 这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
#
# 解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法：
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__

# 2、__iter__
# 若一个类要用于for..。in循环，需使用__iter__()方法返回一个迭代对象
# Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

# 斐波那契数列
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 #初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 1000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

for n in Fib():
    print(n)
# 1
# 1
# 2
# 3
# 5
# ...
# 610
# 987


# 3、__getitem__
# Fib实例无法获取当中的元素
# print(Fib()[5]) # TypeError: 'Fib' object is not subscriptable -- 该实例对象不支持下标访问

# 要像list一样按照下标取出元素，需使用__getitem()方法
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

f = Fib()
print(f[1]) # 1
print(f[2]) # 2
print(f[3]) # 3
print(f[10]) # 89
print(f[100]) # 573147844013817084101


# Fib实例获取一段范围内的元素：实现切片，__getitem()方法传入的参数可以是一个int，也可以是一个切片对象
class Fib(object):
    def __getitem__(self, n): # n是索引 or 切片
        if isinstance(n, int): # n是索引
            a,b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start == None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
# 测试slice
f = Fib()
print(f[0:5])
print(f[:10])
print(f[:10:2]) # 但现有函数未对切片的step参数、负数等未作处理，该函数有许多需要改进的地方

# 若将对象看成dict，则__getitem()的参数 n 也可能是一个可以作key的object，例如str
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。
# 最后，还有一个__delitem__()方法，用于删除某个元素。

# 总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，
# 这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口


# 4、__getattr__
# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。
class Student(object):

    def __init__(self):
        self.name = 'Michael'

s = Student()
print(s.name) # 调用name属性无问题
# print(s.score) 调用不存在的score会报错 AttributeError: 'Student' object has no attribute 'score'

# 若要避免报错，一个方法是加上score属性，
# 另一种方法：在Python的有一种机制，就是写一个__getattr()方法，动态的返回一个属性
class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99

# 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，
# 这样，我们就有机会返回score的值：
s = Student()
print(s.name) # Michael
print(s.score) # 99

# __getattr__也可以返回函数
class Student(object):

    def __getattr__(self, attr):
        if attr == 'age':
            return lambda:25

# lambda:无参匿名函数，t = lambda:True   测试：print(t())
# 等价于def func(): return True  测试：print(func())
s = Student()
print(s.age()) # 25

# 注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。

# 此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：

class Student(object):

    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
# 这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。

# 这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。

# 现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：
#
# http://api.server/user/friends
# http://api.server/user/timeline/list
# 如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。
#
# 利用完全动态的__getattr__，我们可以写出一个链式调用：
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.user.timeline.list)

# __call__
# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。
# 能不能直接在实例本身上调用呢？在Python中，答案是肯定的。
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。
class Student(object):

    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('Michael')
print(s())

# __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。
#
# 如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。
#
# 那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例：

class Student1(object):

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs): #__call__()还可以定义参数
        pass

# 怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，
# 比如函数和我们上面定义的带有__call__()的类实例：
print(callable(Student('Michael'))) # True
print(callable(max)) # True
print(callable([1, 2, 3])) # False
print(callable(None)) # False
print(callable('str')) # False

# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

class Husky(Dog):# Husky 哈士奇
    def run(self):
        print('Husky is running...')

# 获取对象信息
# 获取对象类型:type()
# 1、基本类型的获取
print(type(123)) # <class 'int'>
print(type('str')) # <class 'str'>
print(type(None)) # <class 'NoneType'>
# 2、一个变量 --> 指向函数或者类
print(abs) # <built-in function abs>
a = Animal()
print(a) # <__main__.Animal object at 0x0000021D16EB2460>

# type()返回的是class类型
# 判断两个变量的type类型是否相同
# 1、一个对象为基本类型
print(type(123) == type(456)) # True
print(type(123) == int) # True
print(type('abc') == type('123')) # True
print(type('abc') == str) # True
print(type('abc') == type(123)) # False

# 2、一个对象为函数:可使用types模块中定义的常量
import types
def fn():
    pass

print(fn == types.FunctionType) # False
print(abs == types.BuiltinFunctionType) # False
print(type(lambda x: x) == types.LambdaType) # True
print(type((x for x in range(10))) == types.GeneratorType) # True

# 继承的class类，判断其类型可使用isinstance()函数
a = Animal()
d = Dog()
h = Husky()

print(isinstance(h,Husky)) # True
print(isinstance(h, Dog)) # True
print(isinstance(h, Animal)) # True
print(isinstance(d, Dog) and isinstance(d, Animal)) # True
print(isinstance(d, Husky)) # False

# 用于基本类型判断
print(isinstance('a', str)) # True
print(isinstance(123, int)) # True
print(isinstance(b'a', bytes)) # True

# 用于 list or tuple 的判断
print(isinstance([1, 2, 3], (list, tuple))) # True
print(isinstance((1, 2, 3), (list, tuple))) # True

# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。

# 获得一个对象的所有属性和方法：使用dir()
print(dir('ABC'))
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__',
# '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__',
# '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
# '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
# '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__',
# '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center',
# 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format',
# 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal',
# 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable',
# 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip',
# 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace',
# 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
# 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate',
# 'upper', 'zfill']

# 在Python中，调用len()函数，实际上，在其内部会自动去调用该对象的__len--()方法
# 下方；两个是等价的
print(len('ABC')) # 3
print('ABC'.__len__()) # 3

# 若在自定义类中使用len(myObj)，则需自定义一个len()方法
class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
print(len(dog)) # 100

# 还有一些普通方法，；如lower()返回小写的字符串
print('ABC'.lower()) # abc

# 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()
# 测试 对象 的属性
print(hasattr(obj,'x')) # 有属性'x'吗？
# True
print(obj.x)
# 9
print(hasattr(obj,'y')) # 有属性'y'吗？
# True
print(setattr(obj,'y',19)) # 设置一个属性'y'
print(hasattr(obj,'y')) # 有属性'y'吗？
# 19
print(getattr(obj,'y')) # 获取属性'y'
# 19
print(obj.y) # 获取属性'y'
#
print(getattr(obj,'z')) # 获取属性'z'
# AttributeError: 'MyObject' object has no attribute 'z'
print(getattr(obj,'z',404)) # 获取属性'z'，如果不存在，返回默认值404
# 404

# 获取 对象 的方法
print(hasattr(obj,'power')) # 有属性'power'吗？
# True
print(getattr(obj,'power')) # 获取属性'power'
# <bound method MyObject.power of <__main__.MyObject object at 0x0000023CA1E8E490>>
fn = getattr(obj,'power') # 获取属性'power'并赋值到变量fn
print(fn) # fn指向obj.power
# <bound method MyObject.power of <__main__.MyObject object at 0x0000023CA1E8E490>>
print(fn()) # 调用fn()与调用obj.power()是一样的
# 81

# 【注】只有在不知道对象信息的情况下，才需要获取对象信息
sum = obj.x + obj.y
sum = getattr(obj,'x') + getattr(obj,'y') # 这种形式没有必要写

# 这类函数正确的用法
def readImage(fp):
    if hasattr(fp,'read'):
        return readData(fp)
    return None






















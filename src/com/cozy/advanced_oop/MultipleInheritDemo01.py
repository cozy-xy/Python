# 多重继承
# 1、Animal -> Mammal , Bird（哺乳动物，鸟类）
#    Mammal -> Dog , Bat（狗狗，蝙蝠）; Bird -> Parrot , Ostrich（鹦鹉，鸵鸟）
# 2、Animal -> Runnable , Flyable（能跑，能飞）
#    Runnable -> Dog , Ostrich（狗狗，鸵鸟）; Flyable -> Parrot , Bat（鹦鹉，蝙蝠）
# 3、Animal -> Mammal , Bird（哺乳动物，鸟类）
#    Mammal -> MRun -> Dog , Mammal -> MFly -> Bat（狗狗，蝙蝠）;
#    Bird -> MRun -> Ostrich , Bird -> MFly -> Parrot（鸵鸟，鹦鹉）

# 多重继承

class Animal(object):
    pass

# 大类：
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物：
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

# 动物功能：能跑，能飞，只需要先定义好Runnable和Flyable的类：
class RunnableMixIn(object):
    def run(self):
        print('Running...')

class FlyableMixIn(object):
    def fly(self):
        print('Flying...')

# 对于需要Runnable功能的动物，就多继承一个Runnable，例如Dog:
class Dog(Mammal, RunnableMixIn):
    pass

# 对于需要Flyable功能的动物，就多继承一个Flyable，例如Bat：
class Bat(Bird, FlyableMixIn):
    pass

# 通过多重继承，一个子类就可以同时获得多个父类的所有功能。

# MixIn
# 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。
# 但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。
# 这种设计通常称之为MixIn。

# 动物分为肉食动物，植食动物
class CarnivorousMixIn(object): # 肉食动物
    pass

class HerbivoresMixIn(object): # 植食动物
    pass

class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass

# MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。
# Python自带的很多库也使用了MixIn。举个例子，Python自带了TCPServer和UDPServer这两类网络服务，而要同时服务多个用户就必须使用多进程或多线程模型，这两种模型由ForkingMixIn和ThreadingMixIn提供。通过组合，我们就可以创造出合适的服务来。

from socketserver import TCPServer, UDPServer

# 网络服务同时服务多个用户 -> 必须使用多进程或多线程模型
class ForkingMixIn(object): # 多进程模型
    pass

class ThreadingMixIn(object): # 多线程模型
    pass

class CoroutineMixIn(object):
    pass

# 比如，编写一个多进程模式的TCP服务，定义如下：
class MyTCPServer(TCPServer, ForkingMixIn):
    pass

# 编写一个多线程模式的UDP服务，定义如下：
class MyUDPServer(UDPServer, ThreadingMixIn):
    pass

# 如果你打算搞一个更先进的协程模型，可以编写一个CoroutineMixIn：
class MyTCPServer(TCPServer, CoroutineMixIn):
    pass
# 这样一来，我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类。

# 由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。
# 只允许单一继承的语言（如Java）不能使用MixIn的设计。
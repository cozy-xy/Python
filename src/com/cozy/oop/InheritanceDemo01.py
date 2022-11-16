# 封装（Encapsulation）、继承（Inheritance）、多态（Polymorphism）
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    pass

class Cat(Animal):
    pass

# 继承：子类获得父类的全部功能
dog = Dog()
print(dog.run()) # Animal is running...

cat = Cat()
print(cat.run()) # Animal is running...

# 继承：子类和父类都存在相同的run()方法时，子类的run()覆盖了父类的run()
class Dog(Animal):

    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

dog = Dog()
print(dog.run()) # Dog is running...

cat = Cat()
print(cat.run()) # Cat is running...

# 多态：当我们定义一个class的时候，我们实际上就定义了一种数据类型。
# 我们定义的数据类型和Python自带的数据类型，比如str、list、dict没什么两样
a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型


# 判断一个变量是否是某个类型，用isinstance判断
print(isinstance(a, list)) # True
print(isinstance(b, Animal)) # True
print(isinstance(c, Dog)) # True

# 一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类
print(isinstance(c, Animal)) # True

# 反之，不行：Dog可以看成Animal，但Animal不可以看成Dog
b = Animal()
print(isinstance(b, Dog())) # False

# 写一个函数，这个函数接受一个Animal类型的变量：
def run_twice(animal):
    animal.run()
    animal.run()

print(run_twice(Animal()))
print(run_twice(Dog()))
print(run_twice(Cat()))

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

print(run_twice(Tortoise()))

# 静态语言 vs 动态语言
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
# 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。



























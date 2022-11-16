# 类与实例
# 关键字  类名   该类是从哪个类继承下来
class Student(object):
    pass

# 根据类创建出实例
bart = Student()

print(bart)
# 变量bart指向的就是一个Student的实例，后面的0x10a67a590是内存地址，每个object的地址都不一样
# <__main__.Student object at 0x000001AC1DBBCF70>

print(Student)
# Student本身则是一个类
# <class '__main__.Student'>

# 给实例变量绑定属性
bart.name = 'Bart Simpson'
print(bart.name)

# 建立模板
# 在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
# 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去
class Student(object):

    def __init__(self,name,score):
        self.name = name
        self.score = score

# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，
# 但self不需要传，Python解释器自己会把实例变量传进去：
bart = Student('Bart Simpson', 59)
print(bart.name)  # Bart Simpson
print(bart.score) # 59

# 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。
# 除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。

# 数据封装



































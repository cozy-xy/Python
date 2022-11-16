class Student(object):
    pass

s = Student()
s.name = 'Michael' # 给实例绑定一个属性
print(s.name)

# 给实例绑定一个方法
def set_age(self,age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age,s) #给实例绑定一个方法
s.set_age(25) #调用实例方法
print(s.age)

# 给实例A的方法，对实例B是不起作用的
s2 = Student()
s2.set_age(25)
# Traceback (most recent call last):
# AttributeError: 'Student' object has no attribute 'set_age'

# 为了给所有实例绑定方法：可以给class绑定方法
def set_score(self,score):
    self.score = score

Student.set_score = set_score # 给class绑定方法，所有实例均可调用
s.set_score(100)
print(s.score) # 100

s2.set_score(99)
print(s2.score) # 99
# 通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。

# 限制实例的属性，比如，只允许对 Student 实例添加 name 和 age 属性
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
class Student(object):
    __slots__ = ('name','age') # 用tuple定义允许绑定的属性名称

s = Student() # 创建新的实例
s.name = 'Michael' # 绑定属性'name'
s.age = 25 # 绑定属性'age'
s.score = 99 # 绑定属性'score'
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# AttributeError: 'Student' object has no attribute 'score'

# 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。
#
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：

class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 9999
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
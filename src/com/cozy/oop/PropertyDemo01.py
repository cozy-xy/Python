# 实例属性 & 类属性

# 1、给实例绑定属性：通过实例变量/self变量
class Student(object):
    def __init__(self,name):
        self.name = name

s = Student('Bob')
s.score = 90

# 2、给Student类本身绑定属性
# 可以直接在class中定义属性，这种属性是类属性，归Student类所有：
class Student(object):
    name = 'Student'

# 当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。来测试一下：

class Student(object):
    name = 'Student'

s = Student() # 创建实例s
print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
# Student
print(Student.name) # 打印类的name属性
# Student
s.name = 'Michael' # 给实例绑定name属性
print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
# Michael
print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
# Student
del s.name # 如果删除实例的name属性
print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
# Student


# 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count = Student.count + 1


# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
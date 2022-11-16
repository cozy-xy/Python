# 访问限制

class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))    # 实例的变量名，以__开头，是一个私有变量（private）

bart = Student('Bart Simpson', 59)
# print(bart.name)
# AttributeError: 'Student' object has no attribute 'name'


class Student(object):

    # 以__为开头和结尾的，是特殊变量，他可直接访问
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    # 外部代码获取 name & score
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    # 允许外部代码修改 score 通过set方法可以对参数进行检查，避免输入无效的参数
    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score') # 捕获异常

# 注意：以下写法
bart = Student('Bart Simpson', 59)
print(bart.get_name())  # Bart Simpson
bart.__name = 'New Name'
print(bart.__name)  # New Name
# 表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！
# 内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。不信试试：

print(bart.get_name()) # get_name()内部返回self.__name
# 'Bart Simpson'


# __开头的实例变量不能直接外部访问，但是可以通过_Student__name访问（因为Python解释器把__name变量改成了_Student_name）
print(bart._Student__name)

# 练习：
# 请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
class Student(object):

    def __init__(self,name,gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self,gender):
        if (gender == 'male') | (gender == 'female'):
            self.__gender = gender
        else:
            raise ValueError('bad gender')


bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')



























































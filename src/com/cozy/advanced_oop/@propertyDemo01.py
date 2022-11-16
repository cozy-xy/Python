# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：

class Student(object):
    pass

s = Student()
s.score = 9999
# 这显然不合逻辑。为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，
# 这样，在set_score()方法里，就可以检查参数：

# 利用getter，setter方法来进行参数检查
class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.set_score(60)
print(s.get_score()) # 60
# s.set_score(9999) # ValueError: score must between 0 ~ 100!


# 利用 @property 装饰器将getter，setter方法变成属性来进行调用
class Student(object):

    # 1、将getter方法变成属性
    @property
    def score(self):
        return self._score

    # 2、@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60
print(s.score) # 60
# s.score = 9999 # ValueError: score must between 0 ~ 100!

# @property还可以定义只读属性-只定义getter方法，不定义setter方法
class Student(object):

    # birth是可读可写
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    # age是仅可读，因为age可以根据birth和当前时间计算出来。
    @property
    def age(self):
        return 2015 - self._birth

# 要特别注意：属性的方法名不要和实例变量重名。例如，以下的代码是错误的：

class Student(object):

    # 方法名称和实例变量均为birth:
    @property
    def birth(self):
        return self.birth
# 这是因为调用s.birth时，首先转换为方法调用，在执行return self.birth时，又视为访问self的属性，
# 于是又转换为方法调用，造成无限递归，最终导致栈溢出报错RecursionError。

# 练习：请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height

# 测试
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

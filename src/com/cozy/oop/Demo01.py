# 面向过程
# 用dict表示学生成绩
std1 = {'name':'Michael','score':98}
std2 = {'name':'Bob','score':81}

# 打印学生成绩：可用函数实现
def print_score(std):
    print('%s：%s' % (std['name'],std['score']))

# 面向对象
# Student这种数据类型应该被视为一个对象，这个对象拥有name和score这两个属性（Property）
# 如果要打印一个学生的成绩，首先必须创建出这个学生对应的对象，然后，给对象发一个print_score消息，让对象自己把自己的数据打印出来。
class Student(object):

    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name,self.score))

# 给对象发消息实际上就是调用对象对应的关联函数，我们称之为对象的方法（Method）
bart = Student('Bart Simpson',59)
lisa = Student('Lisa Simpson',87)
bart.print_score()
lisa.print_score()

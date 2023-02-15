# collections是Python内建的一个集合模块，提供了许多有用的集合类。
#
# 1、namedtuple
# 我们知道tuple可以表示不变集合，例如，一个点的二维坐标就可以表示成：

p = (1, 2)
# 但是，看到(1, 2)，很难看出这个tuple是用来表示一个坐标的。
#
# 定义一个class又小题大做了，这时，namedtuple就派上了用场：
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x) # 1
print(p.y) # 2

# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
#
# 这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。
#
# 可以验证创建的Point对象是tuple的一种子类：
print(isinstance(p, Point)) # True
print(isinstance(p, tuple)) # True

# 类似的，如果要用坐标和半径表示一个圆，也可以用namedtuple定义：
# namedtuple('名称', [属性list]):
Circle = namedtuple('Circle', ['x', 'y', 'r'])

# 2、deque
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
#
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q) # deque(['y', 'a', 'b', 'c', 'x'])
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。

# 3、defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1']) # key1存在 abc
print(dd['key2']) # key2不存在，返回默认值 N/A

# 注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
#
# 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。

# 4、OrderedDict
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
#
# 如果要保持Key的顺序，可以用OrderedDict：
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)]) # dict的Key是无序的
print(d) # {'a': 1, 'b': 2, 'c': 3}
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)]) # OrderedDict的Key是有序的
print(od) # OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(list(od.keys())) # 按照插入的Key的顺序返回
# ['z', 'y', 'x']

# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity     # 设置容量参数

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0 # if b in a -> b在a中；else -> b不在a中     # 如果将传入的key已有，则containsKey为1，反之0
        if len(self) - containsKey >= self._capacity:     # 如果原本key数目大于等于容量，且不是传入重复的key
            last = self.popitem(last=False)          # 以先进先出的原则，移除最早添加的元素
            print('remove:', last)          # 打印：移除最早添加的元素
        if containsKey:
            del self[key]          # 如果传入相同的key，则删除旧的key
            print('set:', (key, value))        # 打印：设置key新的value
        else:
            print('add:', (key, value))       # 打印：添加新key与value
        OrderedDict.__setitem__(self, key, value)

# 5、ChainMap
# ChainMap可以把一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找。
#
# 什么时候使用ChainMap最合适？举个例子：应用程序往往都需要传入参数，参数可以通过命令行传入，可以通过环境变量传入，还可以有默认参数。
# 我们可以用ChainMap实现参数的优先级查找，即先查命令行参数，如果没有传入，再查环境变量，如果没有，就使用默认参数。
#
# 下面的代码演示了如何查找user和color这两个参数：
from collections import ChainMap
import os, argparse

# （1）构造缺省参数:
defaults = {
    'color': 'red',
    'user': 'guest'
}

# （2）构造命令行参数:
parser = argparse.ArgumentParser()    #创建对象
parser.add_argument('-u', '--user')     # 添加命令行参数
parser.add_argument('-c', '--color')
namespace = parser.parse_args()      # 解析命令行参数
command_line_args = { k: v for k, v in vars(namespace).items() if v }

# 1.1 列表推导式
# 语法：
# [表达式 for 变量 in 列表]
# 代表从列表中取出每个元素，然后在按照表达式运算，然后放在新的列表中
#
# [表达式 for 变量 in 列表 if 条件]
# 代表从列表中取出满足条件的元素，然后在按照表达式运算，然后放在新的列表中
# f
# 例1: 过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
print([name.upper() for name in names if len(name)>3])

# 1.2 字典推导式
# 语法  { key: value for 变量 in 数据集 if 条件}
# 列如：
from random import randint
data ={n : randint(10,100) for n in range(10)}
print(data)
# 过滤value大于90
data2  = { k:v for k,v in data.items() if v>=90}
print(data2)

# 1.3 集合推导式
# 语法 { 表达式 for value in 数据集 if 条件 }
# 列如：
# 用集合推导建字符串长度的集合
strings = ['a','is','with','if','file','exception']
{len(s) for s in strings}    #有长度相同的会只留一个，这在实际上也非常有用
# 2 提高访问元组的可读性
student=('张三','22','北京市，海定区')



# （3）组合成ChainMap:
combined = ChainMap(command_line_args, os.environ, defaults) # 先查命令行参数，再查环境变量，最后默认参数

# （4）打印参数:
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])


# 没有任何参数时，打印出默认参数：
# $ python3 use_chainmap.py
# color=red
# user=guest

# 当传入命令行参数时，优先使用命令行参数：
# $ python3 use_chainmap.py -u bob
# color=red
# user=bob

# 同时传入命令行参数和环境变量，命令行参数的优先级较高：
# $ user=admin color=green python3 use_chainmap.py -u bob
# color=green
# user=bob

# 6、Counter
# Counter是一个简单的计数器，例如，统计字符出现的个数：
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c) # Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})
c.update('hello') # 也可以一次性update
print(c)  # Counter({'r': 2, 'o': 2, 'g': 2, 'm': 2, 'l': 2, 'p': 1, 'a': 1, 'i': 1, 'n': 1, 'h': 1, 'e': 1})

# Counter实际上也是dict的一个子类，上面的结果可以看出每个字符出现的次数。


















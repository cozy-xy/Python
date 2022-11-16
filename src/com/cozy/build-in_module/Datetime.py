# datetime是Python处理日期和时间的标准库。
#
# 获取当前日期和时间
# 我们先看如何获取当前日期和时间：
from datetime import datetime
now = datetime.now() # 获取当前datetime
print(now)
# 2022-10-13 14:41:29.245279
print(type(now))
# <class 'datetime.datetime'>
# 注意到datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类。
#
# 如果仅导入import datetime，则必须引用全名datetime.datetime。
#
# datetime.now()返回当前日期和时间，其类型是datetime。
#
# 获取指定日期和时间
# 要指定某个日期和时间，我们直接用参数构造一个datetime：
from datetime import datetime
dt = datetime(2022, 10, 13, 14, 48) # 用指定日期时间创建datetime
print(dt)

# datetime转换为timestamp
# 在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。
#
# 你可以认为：
# timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
# 对应的北京时间是：
# timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00
# 可见timestamp的值与时区毫无关系，因为timestamp一旦确定，其UTC时间就确定了，转换到任意时区的时间也是完全确定的，这就是为什么计算机存储的当前时间是以timestamp表示的，因为全球各地的计算机在任意时刻的timestamp都是完全相同的（假定时间已校准）。
#
# 把一个datetime类型转换为timestamp只需要简单调用timestamp()方法：

from datetime import datetime
dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
dt.timestamp() # 把datetime转换为timestamp
1429417200.0
# 注意Python的timestamp是一个浮点数，整数位表示秒。
#
# 某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。
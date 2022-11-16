# 调试
# 1、print()
def foo(s):
    n = int(s)
    print('>>> n = %d' % n)
    return 10 / n

def main():
    foo('0')

main()

# 2、断言：assert
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')
# assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
# 如果断言失败，assert语句本身就会抛出AssertionError：

# 启动Python解释器时可以用-O参数来关闭assert：
#
# $ python -O err.py
# Traceback (most recent call last):
# ...
# ZeroDivisionError: division by zero
# 注意：断言的开关“-O”是英文大写字母O，不是数字0。
# 关闭后，你可以把所有的assert语句当成pass来看。

# 3、logging
import logging  #logging.info()就可以输出一段文本。运行，发现除了ZeroDivisionError，没有任何信息
# 在import logging之后添加一行配置再试试：
logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
# INFO:root:n = 0
# Traceback (most recent call last):
#   File "err.py", line 8, in <module>
#     print(10 / n)
# ZeroDivisionError: division by zero

# 这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，
# 当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。
# 这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
#
# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。

# 4、pdb：启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态

# 5、IDE：如果要比较爽地设置断点、单步执行，就需要一个支持调试功能的IDE

# 1、StringIO

# StringIO就是在内存中创建的file-like Object，常用作临时缓冲。
# 很多时候，数据读写不一定是文件，也可以在内存中读写。
# StringIO顾名思义就是在内存中读写str。

# 要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：
from io import StringIO
f = StringIO()
print(f.write('hello')) # 5
print(f.write(' ')) # 1
print(f.write('world!')) # 6
print(f.getvalue()) # getvalue()方法用于获得写入后的str。hello world!

# 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
from io import StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
# Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）或字符序列。
# 注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
# Hello!
# Hi!
# Goodbye!

# 2、BytesIO

# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
# BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：
from io import BytesIO
f = BytesIO()
print(f.write('中文'.encode('utf-8'))) # 6
print(f.getvalue()) # b'\xe4\xb8\xad\xe6\x96\x87'
# 请注意，写入的不是str，而是经过UTF-8编码的bytes。

# 和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：
from io import BytesIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read()) # b'\xe4\xb8\xad\xe6\x96\x87'

# StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。


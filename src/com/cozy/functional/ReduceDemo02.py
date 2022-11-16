# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# reduce(f,[x1,x2,x3,x4]) = f(f(f(x1,x2),x3),x4)

# 序列求和
from functools import reduce
def add(x,y):
    return x + y
print(reduce(add,[1,3,5,7,9]))


# ===============================================================

# 将序列[1,3,5,7,9]变换为整数13579
from functools import reduce
def fn(x,y):
    return x * 10 + y
print(reduce(fn,[1,3,5,7,9]))


# ===============================================================


# 字符串转变为整数
from functools import reduce
def fn(x,y):
    return x * 10 + y

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

print(reduce(fn,map(char2num,'13579')))

# 字符串转变为整数：整理合并
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

# 字符串转变为整数：使用lambda函数简化
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


# ===============================================================

# 练习：利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    result = name[0].upper() + name[1:].lower()
    return result

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)




# ===============================================================

# 练习：Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    return reduce(lambda x, y : x * y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')




# ===============================================================

# 练习：利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    def fn(x,y):
        return x*10 + y
    n = s.index('.')
    s1 = list(map(int,[x for x in s[:n]]))
    s2 = list(map(int,[x for x in s[n+1:]]))
    return reduce(fn,s1) + reduce(fn,s2)/10**len(s2)   # m**n --> m的n次方


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')










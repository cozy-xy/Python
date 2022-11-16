# 计算 x^2
def power(x):
    return x * x

# 计算 x^n
def power(x,n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

# 默认参数
def power(x,n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

# print(power(5))
# print(power(5,2))

# 一年级小学生注册信息
def enroll(name,gender):
    print('name:',name)
    print('gender:',gender)

print(enroll('Sarah','F')) # name: Sarah
                           # gender: F
                           # None

# 在上述基础上继续传入年龄、城市等信息
# 可以将年龄、城市设为默认参数
def enroll(name,gender,age = 6,city = 'Beijing'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)

print(enroll('Sarah','F'))
# 结果：
#       name: Sarah
#       gender: F
#       age: 6
#       city: Beijing
#       None

# 与默认参数不符合的学生需提供额外的信息
print(enroll('Bob','M',7))
print(enroll('Adam','M',city='Tianjin'))
# 结果：
#       name: Bob
#       gender: M
#       age: 7
#       city: Beijing
#       None
#       name: Adam
#       gender: M
#       age: 6
#       city: Tianjin
#       None

# 默认参数的避雷点
def add_end(L = []):
     L.append('END')
     return L

print(add_end([1,2,3])) # [1, 2, 3, 'END']
print(add_end()) # ['END']
print(add_end()) # ['END', 'END']
# 函数似乎每次都“记住了”上次添加了'END'后的list

# 修改上述例子
def add_end(L = None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end([1,2,3])) # [1, 2, 3, 'END']
print(add_end()) # ['END']
print(add_end()) # ['END']

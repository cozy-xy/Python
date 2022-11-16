# 关键字参数
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)

# 调用函数时，可以只传入必选参数
print(person('Michael',30))  # name: Michael age: 30 other: {}
                             # None

# 传入任意个数的关键字参数
print(person('Bob',35,city = 'Beijing')) # name: Bob age: 35 other: {'city': 'Beijing'}
                                         # None

# 比如：一个学生注册，用户名，年龄是必填项，其他都是可选项，可以用关键字参数来满足这一需求
# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
extra = {'city':'Beijing','job':'Engineer'}
print(person('Jack',24,city=extra['city'],job=extra['job']))
# name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
# None

# 将上述代码简化
extra = {'city':'Beijing','job':'Engineer'}
print(person('Jack',24,**extra))
# name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
# None


# 命名关键字参数

# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数
# 对于传入哪些关键字参数，需要在函数内部通过kw检查
# 检查person()函数中是否有city和job参数
def person(name,age,**kw):
    if 'city' in kw:
        pass # 有city参数
    if 'job' in kw:
        pass # 有job参数
    print('name:',name,'age:',age,'other:',kw)

print(person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456))
# name: Jack age: 24 other: {'city': 'Beijing', 'addr': 'Chaoyang', 'zipcode': 123456}
# None
# 调用者仍可以传入不受限制的关键字参数

# 若要限制关键字参数的名字，就可用命名关键字参数
def person(name,age,*,city,job):
    print(name,age,city,job)

print(person('Jack', 24, city='Beijing', job='Engineer'))
# Jack 24 Beijing Engineer
# None

# 函数定义中有一个可变参数，则在其后的命名关键字参数无需 *
def person(name,age,*args,city,job):
    print(name,age,args,city,job)

# 命名关键字参数必须传入参数名，否则调用参数会报错
print(person('Jack', 24, 'Beijing', 'Engineer')) # 报错


# 命名关键字参数可以有缺省值，从而简化调用：
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)

# 由于命名关键字参数city具有默认值，调用时，可不传入city参数：
print(person('Jack', 24, job='Engineer'))
# Jack 24 Beijing Engineer
# None

# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。
# 如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：
def person(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass
























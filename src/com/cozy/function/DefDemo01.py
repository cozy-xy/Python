def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(0)) # 0
print(my_abs(-11)) # 11

# 空函数
def nop():
    pass

# 参数检查
print(abs('a')) # 会类型报错
print(my_abs('a')) # 不会报类型错误

# 修改my_abs()函数
def my_abs(x):
    # 给参数作限制
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


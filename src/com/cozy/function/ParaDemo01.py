# 位置参数
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

print(power(5,2))





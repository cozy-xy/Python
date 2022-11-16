# 可变参数
# 计算 a^2 + b^2 + c^2 + ...
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# 调用时组装一个list或tuple
print(calc([1,2,3])) # 14
print(calc((1,2,3,5,7))) # 88

# 若利用可变参数，调用函数可以简化
# 将函数参数改为可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1,2)) # 5
print(calc()) # 0

# 若已有一个list或tuple，如何调用一个可变参数
nums = [1,2,3]
print(calc(nums[0],nums[1],nums[2]))  # 14
# 改进上述方法
nums = [1,2,3]
print(calc(*nums))  # 14

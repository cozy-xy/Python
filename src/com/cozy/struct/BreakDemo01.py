# 循环打印1～100的数字
n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')

# 提前结束循环
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')
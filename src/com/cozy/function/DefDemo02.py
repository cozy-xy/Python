import math

# 在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的坐标：
def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny

x,y = move(100,100,60,math.pi / 6)
print(x,y) # 151.96152422706632 70.0

r = move(100,100,60,math.pi / 6)
print(r) # (151.96152422706632, 70.0)
# 返回值是一个tuple


# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0 的两个解。
def quadratic(a,b,c):
    m1 = (-b + math.sqrt(b*b - 4*a*c)) / (2*a)
    m2 = (-b - math.sqrt(b*b - 4*a*c)) / (2*a)
    return m1,m2


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
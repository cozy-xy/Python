# 递归函数

# 计算阶乘 n! = 1 x 2 x 3 x ... x n
# 用函数fact(n)表示，阶乘英文：factorial
# fact(n)=n!=1×2×3×⋅⋅⋅×(n−1)×n=(n−1)!×n=fact(n−1)×n
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print(fact(5)) # 120
print(fact(1000)) # RecursionError: maximum recursion depth exceeded

# 尾递归
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


# 汉诺塔问题
# 请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法
# def move(n,a,b,c):
#     if n == 1:
#         print(a,'-->',c)
#     return
#
# print(move(3,'A','B','C'))


# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(3, 'A', 'B', 'C')
# move A --> C
# move A --> B
# move C --> B
# move A --> C
# move B --> A
# move B --> C
# move A --> C


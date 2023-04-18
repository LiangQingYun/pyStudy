# 绝对值函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-1))


# 空函数
def nop():
    pass


# 缺省参数  只能放在最后
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# 可变参数  *元组   **字典
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum


# **kw  关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Michael', 30, city='Beijing', job='Engineer')

# 匿名函数
fun = lambda x: x * x
print(fun(5))

# 匿名函数
f2 = lambda x, y: x * x + y * y

def run(desc, f):
    print(desc)
    return f(2,3)

print(run('匿名函数 计算2平方+3平方=', f2))

#递归函数
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(5))



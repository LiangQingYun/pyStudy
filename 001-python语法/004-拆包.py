# 元组拆包
print('\n元组拆包')
coordinates = (3, 5)
x, y = coordinates
print("x:", x)  # 输出 x: 3
print("y:", y)  # 输出 y: 5

# 列表拆包
print('\n列表拆包')
colors = ['red', 'green', 'blue']
c1, c2, c3 = colors
print("c1:", c1)  # 输出 c1: red
print("c2:", c2)  # 输出 c2: green
print("c3:", c3)  # 输出 c3: blue

# 集合拆包
print('\n集合拆包')
my_set = {'apple', 'banana', 'orange', 'kiwi'}
fruit1, fruit2, fruit3, fruit4 = my_set
print(fruit1)  # 'kiwi'
print(fruit2)  # 'orange'
print(fruit3)  # 'apple'
print(fruit4)  # 'banana'

# 字典拆包
print('\n字典拆包')
my_dict = {'name': 'Alice', 'age': 25, 'gender': 'female'}
name, age, gender = my_dict
print(name)  # 'name'
print(age)  # 'age'
print(gender)  # 'gender'

# 函数返回值拆包
print('\n函数返回值拆包')


def divide(num1, num2):
    quotient = num1 // num2
    remainder = num1 % num2
    return quotient, remainder


result1, result2 = divide(10, 3)
print(result1, result2)

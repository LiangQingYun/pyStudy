def print_number(*nums):
    print(type(nums))
    for n in nums:
        print(n)

"""
    方法形参是一个可变参数, 加上*后,传入的参数会拆包, 传入的是一个个的参数    接收参数形成一个元组
"""
if __name__ == '__main__':
    ls = [1, 2, 3, 4, 5]
    print_number(ls)
    print_number(*ls)

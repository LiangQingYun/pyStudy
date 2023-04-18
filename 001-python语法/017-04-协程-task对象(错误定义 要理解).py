import asyncio
# 协程函数的定义
async def greeting(name):
    print(f"开始执行.... {name}!")
    await asyncio.sleep(3)  # 模拟耗时操作
    print(f"Hello  {name}!")
    return f"我的名字是{name}!"

"""
    错误的task协程并发定义
"""
async def main_error():
    await asyncio.create_task(greeting("Alice"))
    await asyncio.create_task(greeting("Bob"))
    print("错误等同....")
    # 等同于
    g1 = asyncio.create_task(greeting("Alice"))
    await g1  # 执行了await已经是在等待g1 结果返回了 ,g2都还没有定义
    g2 = asyncio.create_task(greeting("Bob"))
    await g2

"""
    正确的task协程并发定义
"""
async def main():
    g1 = asyncio.create_task(greeting("Alice"))
    g2 = asyncio.create_task(greeting("Bob"))
    await g1
    await g2
    print("正确等同....")
    # todo : 等同于以下代码
    g1 = asyncio.create_task(greeting("Alice"))
    g2 = asyncio.create_task(greeting("Bob"))  # 定义的时候已经开始执行了
    await g1, g2  # 等待结果返回

asyncio.run(main_error())
print("\n")
asyncio.run(main())

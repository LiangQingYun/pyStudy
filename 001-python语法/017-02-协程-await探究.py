import asyncio


# 协程函数的定义
async def greeting(name):
    await asyncio.sleep(5)  # 模拟耗时操作
    print(f"Hello, {name}!")


# 协程函数的定义
async def main():
    # await 用来异步等待协程函数的执行结果
    # 注意 : 当前这里使用await会堵塞代码执行 , 因为await后面跟随的是普通的协程对象 , 要变成异步, 需要使用asyncio.ensure_future()方法
    await greeting("Alice")
    await greeting("Bob")
    await greeting("Charlie")

"""
    用run()方法来启动协程  不用自定义事件循环
    当前代码时一个同步单线程代码
"""

asyncio.run(main())


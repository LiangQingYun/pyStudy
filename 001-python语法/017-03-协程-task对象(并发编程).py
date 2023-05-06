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


"""
    正确的task协程并发定义
"""


async def main(case):
    if case == 1:
        g1 = asyncio.create_task(greeting("Alice"))
        g2 = asyncio.create_task(greeting("Bob"))
        await g1
        await g2
    elif case == 2:
        # 或者在python3.7以前的版本中使用下面的代码
        tasks = []
        for p_name in ["Alice", "Bob"]:
            tasks.append(asyncio.create_task(greeting(p_name)))
        await asyncio.gather(*tasks)
    elif case == 3:
        # 或者在python3.7之后可以使用 todo : 建议使用这种方式
        tasks = []
        for p_name in ["Alice", "Bob"]:
            tasks.append(asyncio.create_task(greeting(p_name)))
        # 使用wait不用拆包
        # 返回值包括两个元素，一个是已完成任务的集合，另一个是未完成任务的集合       python中通常使用 _ 表示一个临时变量，它在这里表示一个不需要使用的变量，只是占位符。
        done, _ = await asyncio.wait(tasks)
        for task in done:
            print(task.result())

"""
    用run()方法来启动协程  不用自定义事件循环
    当前代码时一个同步单线程代码
"""
# asyncio.run(main_error())
asyncio.run(main(3))
"""
    用run可能会报错 : RuntimeError: Event loop is closed 
    可以换方式
"""
loop = asyncio.get_event_loop()
loop.run_until_complete(main(3))


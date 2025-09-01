import asyncio
import threading
import time

# 任务取消
async def cancel_me():
    print('cancel_me(): before sleep')

    try:
        # 等待 1 小时
        await asyncio.sleep(3600)
    except asyncio.CancelledError:
        print('cancel_me(): cancel sleep')
        raise
    finally:
        print('cancel_me(): after sleep')

async def cancel_task():
    task = asyncio.create_task(cancel_me())
    # 等待 1 秒
    await asyncio.sleep(1)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print(f'cancel_task(): {task!r} was canceled')

# 跨线程调度

# 在线程中运行
def blocking_io():
    print(f"start blocking_io at {time.strftime('%X')}")
    # 请注意 time.sleep() 可被替换为任意一种
    # 阻塞式 IO 密集型操作，例如文件操作。
    time.sleep(1)
    print(f"blocking_io complete at {time.strftime('%X')}")
    
async def blocking_demo2():
    print(f"start blocking_demo2 at {time.strftime('%X')}")
    # 请注意 time.sleep() 可被替换为任意一种
    # 阻塞式 IO 密集型操作，例如文件操作。
    time.sleep(1)
    print(f"blocking_demo2 complete at {time.strftime('%X')}")    
async def run_blocking_io():
    print(f"started main at {time.strftime('%X')}")
    await asyncio.gather(
        asyncio.to_thread(blocking_io),
        blocking_demo2())

    print(f"finished main at {time.strftime('%X')}")    

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f


async def main():
    # 将三个调用 *并发地* 加入计划任务：
    L = await asyncio.gather(
        factorial("B", 3),
        factorial("A", 2),
        factorial("C", 4),
    )
    print(L)
    print("Done")


if __name__ == "__main__":
    # asyncio.run(main())
    # asyncio.run(run_blocking_io())
    asyncio.run(cancel_task())
    

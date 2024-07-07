import asyncio

async def fun1():
    print("3")
    await asyncio.sleep(5)
    print("4")
    return"sb"


async def main():
    print("1")
    task1=asyncio.create_task(fun1())
    task2=asyncio.create_task(fun1())
    print ("2")
    r1=await task1
    r2=await task2
    print(r1,r2)


asyncio.run(main())
import asyncio

async def fun1():
    print("fuck")
    await asyncio.sleep(2)
    print("and")

async  def fun2():
    print("wjj")
    await asyncio.sleep(2)
    print("tx")

async def main():
    tasks = [
        asyncio.create_task(fun1()),
        asyncio.create_task(fun2())
    ]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
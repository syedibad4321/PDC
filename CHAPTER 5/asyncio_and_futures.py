import asyncio

async def first_coroutine(num):
    count = 0
    for i in range(1, num + 1):
        count += 1
    await asyncio.sleep(4)
    return f'First coroutine (sum of N ints) result = {count}'

async def second_coroutine(num):
    count = 1
    for i in range(2, num + 1):
        count *= i
    await asyncio.sleep(4)
    return f'Second coroutine (factorial) result = {count}'

async def third_coroutine(num):
    result = " ".join(str(i) for i in range(num, 0, -1))
    await asyncio.sleep(4)
    return f'Third coroutine (reverse count) result = {result}'

async def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    results = await asyncio.gather(
        first_coroutine(num1),
        second_coroutine(num2),
        third_coroutine(num1)
    )

    for res in results:
        print(res)

if __name__ == '__main__':
    asyncio.run(main())


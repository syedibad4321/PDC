import asyncio
import time

async def factorial(number):
    start_time = time.time()
    fact = 1
    for i in range(2, number + 1):
        print(f'Asyncio.Task: Compute factorial({i})')
        await asyncio.sleep(1)
        fact *= i
    end_time = time.time()
    print(f'Asyncio.Task - factorial({number}) = {fact} (Duration: {end_time - start_time:.2f}s)')


async def fibonacci(number):
    start_time = time.time()
    a, b = 0, 1
    for i in range(number):
        print(f'Asyncio.Task: Compute fibonacci({i})')
        await asyncio.sleep(1)
        a, b = b, a + b
    end_time = time.time()
    print(f'Asyncio.Task - fibonacci({number}) = {a} (Duration: {end_time - start_time:.2f}s)')


async def binomial_coefficient(n, k):
    start_time = time.time()
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) / i
        print(f'Asyncio.Task: Compute binomial_coefficient step {i}')
        await asyncio.sleep(1)
    end_time = time.time()
    print(f'Asyncio.Task - binomial_coefficient({n}, {k}) = {result} (Duration: {end_time - start_time:.2f}s)')


async def main():
    # create tasks to run in parallel
    tasks = [
        asyncio.create_task(factorial(10)),
        asyncio.create_task(fibonacci(10)),
        asyncio.create_task(binomial_coefficient(20, 10))
    ]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())

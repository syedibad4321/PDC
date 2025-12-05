import asyncio
import random

# dictionary to track call counts for each task
call_counts = {"task_A": 0, "task_B": 0, "task_C": 0}

async def task_A(end_time, chain_id):
    while asyncio.get_running_loop().time() < end_time:
        call_counts["task_A"] += 1
        print(f"Chain {chain_id}: task_A called (count={call_counts['task_A']})")
        await asyncio.sleep(random.randint(0, 3))
        await task_B(end_time, chain_id)

async def task_B(end_time, chain_id):
    if asyncio.get_running_loop().time() >= end_time:
        return
    call_counts["task_B"] += 1
    print(f"Chain {chain_id}: task_B called (count={call_counts['task_B']})")
    await asyncio.sleep(random.randint(0, 3))
    await task_C(end_time, chain_id)

async def task_C(end_time, chain_id):
    if asyncio.get_running_loop().time() >= end_time:
        return
    call_counts["task_C"] += 1
    print(f"Chain {chain_id}: task_C called (count={call_counts['task_C']})")
    await asyncio.sleep(random.randint(0, 3))
    await task_A(end_time, chain_id)

async def run_chain(chain_id, duration):
    loop = asyncio.get_running_loop()
    end_loop = loop.time() + duration
    await task_A(end_loop, chain_id)

async def main():
    duration = 20  # seconds
    # Run 3 parallel chains
    await asyncio.gather(
        run_chain(1, duration),
        run_chain(2, duration),
        run_chain(3, duration)
    )

    print("\n=== Total Call Counts ===")
    for task, count in call_counts.items():
        print(f"{task}: {count}")

if __name__ == "__main__":
    asyncio.run(main())

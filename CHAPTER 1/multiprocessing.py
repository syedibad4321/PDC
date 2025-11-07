# ======================================
# FACTORIAL PROGRAM (with MULTIPROCESSING)
# ======================================

import multiprocessing
import time


# 🔹 factorial function
def factorial(n):
    """Calculate factorial of a number"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# 🔹 worker function (for multiprocessing)
def calculate_factorial(num, output_list):
    """Each process will calculate factorial of one number"""
    result = factorial(num)
    output_list.append((num, result))


if __name__ == "__main__":
    start_time = time.time()

    # list of numbers to calculate factorial for
    numbers = [5, 7, 8, 10, 12, 15, 18, 20]
    manager = multiprocessing.Manager()
    output_list = manager.list()  # shared list for all processes
    jobs = []

    # 🔹 create multiple processes
    for num in numbers:
        process = multiprocessing.Process(
            target=calculate_factorial,
            args=(num, output_list)
        )
        jobs.append(process)

    # 🔹 start all processes
    for j in jobs:
        j.start()

    # 🔹 wait for all to finish
    for j in jobs:
        j.join()

    # 🔹 print results
    print("\n=== Multiprocessing Factorial Results ===")
    for num, result in sorted(output_list):
        print(f"Factorial of {num} = {result}")

    end_time = time.time()
    print("\nMultiprocessing time =", end_time - start_time, "seconds")

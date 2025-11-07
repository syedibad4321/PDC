# ======================================
# Factorial Calculation using Threads + Barrier
# ======================================

from threading import Barrier, Thread
from time import time
import random

# -----------------------------
# Configuration
# -----------------------------
numbers = [5, 7, 8]  # numbers to calculate factorial
num_workers = len(numbers)

# Barrier ensures all threads finish factorial before printing final results
finish_line = Barrier(num_workers)

# Shared list for results
results = []

# -----------------------------
# Factorial Function
# -----------------------------
def factorial(n):
    """Recursive factorial calculation"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# -----------------------------
# Worker Function
# -----------------------------
def worker(number):
    """Each thread calculates factorial and waits at the barrier"""
    result = factorial(number)
    results.append((number, result))
    # simulate random delay (like race running time)
    sleep_time = random.randint(1, 3)
    from time import sleep
    sleep(sleep_time)
    print(f"Thread for number {number} reached barrier after {sleep_time} sec")
    finish_line.wait()  # wait for all threads

# -----------------------------
# Main Function
# -----------------------------
def main():
    threads = []
    start_time = time()
    print("START FACTORIAL CALCULATION...\n")

    # Start threads
    for number in numbers:
        t = Thread(target=worker, args=(number,))
        threads.append(t)
        t.start()

    # Wait for threads to finish
    for t in threads:
        t.join()

    end_time = time()
    print("\nAll factorials calculated:")
    for num, fact in sorted(results):
        print(f"Factorial of {num} = {fact}")

    print(f"\nTotal time taken: {end_time - start_time:.2f} seconds")

# -----------------------------
# Entry Point
# -----------------------------
if __name__ == "__main__":
    main()

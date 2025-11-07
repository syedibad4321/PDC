import multiprocessing
import time
import os

# -----------------------------
# Factorial Function
# -----------------------------
def factorial(n):
    print(f"Process {multiprocessing.current_process().name} starting factorial of {n}, PID={os.getpid()}")
    result = 1
    for i in range(1, n + 1):
        result *= i
        print(f"Process {multiprocessing.current_process().name} --> step {i}, PID={os.getpid()}")
        time.sleep(0.3)  # simulate work
    print(f"Process {multiprocessing.current_process().name} finished factorial of {n} = {result}")

# -----------------------------
# Main Function
# -----------------------------
if __name__ == '__main__':
    numbers = [3, 4, 5, 6, 7]  # numbers for which factorial will be calculated

    for i, num in enumerate(numbers):
        process = multiprocessing.Process(target=factorial, args=(num,), name=f"FactorialProcess-{i}")
        process.start()
        process.join()  # wait for the process to finish before starting the next

    print("All factorial processes completed.")

import multiprocessing
import time
import os

# -----------------------------
# Factorial Function
# -----------------------------
def factorial(n):
    print(f"{multiprocessing.current_process().name} starting factorial of {n}, PID={os.getpid()}")
    result = 1
    for i in range(1, n + 1):
        result *= i
        print(f"{multiprocessing.current_process().name} --> step {i}, PID={os.getpid()}")
        time.sleep(0.5)
    print(f"{multiprocessing.current_process().name} finished factorial of {n} = {result}, PID={os.getpid()}")
    return result

# -----------------------------
# Worker Function
# -----------------------------
def worker():
    name = multiprocessing.current_process().name
    if name == 'background_process':
        for num in range(3, 6):  # small numbers
            factorial(num)
    else:
        for num in range(6, 9):  # larger numbers
            factorial(num)

# -----------------------------
# Main Function
# -----------------------------
if __name__ == '__main__':
    # Background daemon process
    background_process = multiprocessing.Process(
        name='background_process',
        target=worker
    )
    background_process.daemon = True  # daemon process

    # Non-daemon process
    NO_background_process = multiprocessing.Process(
        name='NO_background_process',
        target=worker
    )
    NO_background_process.daemon = False  # non-daemon

    # Start both processes
    background_process.start()
    NO_background_process.start()

    # Wait for non-daemon process to finish
    NO_background_process.join()
    print("Main process exiting, daemon process may be terminated if still running.")

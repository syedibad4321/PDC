import multiprocessing
import time
import os

# -----------------------------
# Factorial Function
# -----------------------------
def factorial(n):
    print(f"Starting factorial for {n}, PID={os.getpid()}")
    result = 1
    for i in range(1, n + 1):
        result *= i
        print(f"{n}! --> {i} step, PID={os.getpid()}")
        time.sleep(0.5)  # simulate work
    print(f"Finished factorial for {n} = {result}, PID={os.getpid()}")
    return result

# Wrapper function to allow terminate-safe calculation
def factorial_worker(n):
    factorial(n)

# -----------------------------
# Main Function
# -----------------------------
if __name__ == '__main__':
    number = 6  # calculate factorial of 6
    p = multiprocessing.Process(target=factorial_worker, args=(number,))

    print('Process before execution:', p, p.is_alive())
    p.start()
    print('Process running:', p, p.is_alive())

    # Let the process run for a short time, then terminate
    time.sleep(2)  # allow some steps to run
    p.terminate()  # terminate process
    print('Process terminated:', p, p.is_alive())

    p.join()
    print('Process joined:', p, p.is_alive())
    print('Process exit code:', p.exitcode)

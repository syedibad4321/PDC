import threading
import time
import os
from threading import Thread
from random import randint

# -----------------------------
# Lock Definition
# -----------------------------
threadLock = threading.Lock()

# -----------------------------
# Numbers to calculate factorial
# -----------------------------
numbers = [5, 7, 8, 6, 4, 3, 9, 10, 2]

# -----------------------------
# Factorial Function
# -----------------------------
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# -----------------------------
# Thread Class
# -----------------------------
class FactorialThread(Thread):
    def __init__(self, name, number):
        Thread.__init__(self)
        self.name = name
        self.number = number

    def run(self):
        # Calculate factorial
        result = factorial(self.number)
        sleep_duration = randint(1, 5)  # simulate random work duration
        time.sleep(sleep_duration)

        # Thread-safe printing
        threadLock.acquire()
        print(f"---> {self.name} calculated factorial of {self.number} = {result}, "
              f"belonging to process ID {os.getpid()}, slept {sleep_duration} sec\n")
        threadLock.release()

# -----------------------------
# Main Function
# -----------------------------
def main():
    start_time = time.time()

    threads = []

    # Create threads for each number
    for i, number in enumerate(numbers):
        t = FactorialThread(f"Thread#{i+1}", number)
        threads.append(t)

    # Start threads
    for t in threads:
        t.start()

    # Join threads
    for t in threads:
        t.join()

    # End
    print("All factorials calculated.")
    print("--- %s seconds ---" % (time.time() - start_time))

# -----------------------------
# Entry Point
# -----------------------------
if __name__ == "__main__":
    main()

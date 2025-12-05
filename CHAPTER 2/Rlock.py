import threading
import time
import random
import os

# -----------------------------
# RLock Example with Factorial
# -----------------------------
class FactorialBox:
    def __init__(self):
        self.lock = threading.RLock()
        self.results = []

    def calculate(self, number):
        with self.lock:
            result = self.factorial(number)
            self.results.append((number, result))
            return result

    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)

# -----------------------------
# Worker Functions
# -----------------------------
def worker(box, number):
    print(f"Thread started for number {number}")
    sleep_time = random.randint(1, 3)
    time.sleep(sleep_time)  # simulate processing
    result = box.calculate(number)
    with box.lock:  # nested lock safe due to RLock
        print(f"Thread {threading.current_thread().name} calculated factorial of {number} = {result}, "
              f"PID={os.getpid()}, slept {sleep_time} sec")

# -----------------------------
# Main Function
# -----------------------------
def main():
    numbers = [5, 7, 8, 6, 4]  # numbers to calculate factorial
    box = FactorialBox()
    threads = []

    start_time = time.time()

    # Create threads
    for i, num in enumerate(numbers):
        t = threading.Thread(target=worker, args=(box, num), name=f"Thread#{i+1}")
        threads.append(t)
        t.start()

    # Join threads
    for t in threads:
        t.join()

    end_time = time.time()

    print("\nAll factorials calculated:")
    for num, res in sorted(box.results):
        print(f"Factorial of {num} = {res}")

    print(f"\nTotal time taken: {end_time - start_time:.2f} seconds")

# -----------------------------
# Entry Point
# -----------------------------
if __name__ == "__main__":
    main()

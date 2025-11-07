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
        print(f"Thread {

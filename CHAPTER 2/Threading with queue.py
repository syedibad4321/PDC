from threading import Thread
from queue import Queue
import time
import random
import os

# -----------------------------
# Factorial Function
# -----------------------------
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# -----------------------------
# Producer Thread
# -----------------------------
class Producer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(5):
            item = random.randint(3, 10)  # produce number for factorial
            self.queue.put(item)
            print(f'Producer notify: item {item} appended to queue by {self.name}')
            time.sleep(random.randint(1, 2))  # simulate production delay

# -----------------------------
# Consumer Thread
# -----------------------------
class Consumer(Thread):
    def __init__(self, queue, results):
        Thread.__init__(self)
        self.queue = queue
        self.results = results

    def run(self):
        while True:
            try:
                item = self.queue.get(timeout=5)  # wait for item
            except:
                break  # exit if no item for timeout
            result = factorial(item)
            print(f'Consumer notify: factorial of {item} = {result} popped by {self.name}, PID={os.getpid()}')
            self.results.append((item, result))
            self.queue.task_done()
            time.sleep(random.randint(1, 2))  # simulate processing delay

# -----------------------------
# Main Function
# -----------------------------
def main():
    queue = Queue()
    results = []

    # Start producer
    producer = Producer(queue)
    producer.start()

    # Start multiple consumers
    consumers = []
    for i in range(3):
        c = Consumer(queue, results)
        c.start()
        consumers.append(c)

    # Wait for producer to finish
    producer.join()
    # Wait for queue to be empty
    queue.join()
    # Wait for consumers to finish
    for c in consumers:
        c.join()

    print("\nAll factorials calculated:")
    for num, res in sorted(results):
        print(f"Factorial of {num} = {res}")

# -----------------------------
# Entry Point
# -----------------------------
if __name__ == "__main__":
    main()

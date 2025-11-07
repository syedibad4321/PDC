import multiprocessing
import random
import time
import os

# -----------------------------
# Factorial Function
# -----------------------------
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# -----------------------------
# Producer Process
# -----------------------------
class Producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        for _ in range(10):
            number = random.randint(3, 10)  # numbers for factorial
            self.queue.put(number)
            print(f"Producer Process: produced number {number}, PID={os.getpid()}")
            time.sleep(1)
            print(f"Queue size is now {self.queue.qsize()}")

# -----------------------------
# Consumer Process
# -----------------------------
class Consumer(multiprocessing.Process):
    def __init__(self, queue, results):
        multiprocessing.Process.__init__(self)
        self.queue = queue
        self.results = results

    def run(self):
        while True:
            if self.queue.empty():
                break
            number = self.queue.get()
            result = factorial(number)
            self.results.append((number, result))
            print(f"Consumer Process: factorial of {number} = {result}, PID={os.getpid()}")
            time.sleep(1)

# -----------------------------
# Main Function
# -----------------------------
if __name__ == '__main__':
    queue = multiprocessing.Queue()
    manager = multiprocessing.Manager()
    results = manager.list()  # shared list for storing factorial results

    # Start producer and consumer
    producer_process = Producer(queue)
    consumer_process = Consumer(queue, results)

    producer_process.start()
    consumer_process.start()

    producer_process.join()
    consumer_process.join()

    print("\nAll factorials calculated:")
    for num, res in results:
        print(f"Factorial of {num} = {res}")

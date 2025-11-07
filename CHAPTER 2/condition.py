import logging
import threading
import time

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# Shared resources
numbers = []          # items produced by producer
condition = threading.Condition()
MAX_ITEMS = 5         # maximum items in buffer

# -----------------------------
# Factorial Function
# -----------------------------
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# -----------------------------
# Consumer Thread
# -----------------------------
class Consumer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def consume(self):
        with condition:
            if len(numbers) == 0:
                logging.info("No items to consume, waiting...")
                condition.wait()

            num = numbers.pop()
            result = factorial(num)
            logging.info(f"Consumed {num}, factorial = {result}")

            condition.notify()

    def run(self):
        for _ in range(10):
            time.sleep(1)
            self.consume()

# -----------------------------
# Producer Thread
# -----------------------------
class Producer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def produce(self):
        with condition:
            if len(numbers) >= MAX_ITEMS:
                logging.info(f"Buffer full ({len(numbers)} items). Waiting...")
                condition.wait()

            # Produce a random number for factorial
            num = threading.current_thread().ident % 10 + 3  # simple random-ish number
            numbers.append(num)
            logging.info(f"Produced number: {num}, buffer size = {len(numbers)}")

            condition.notify()

    def run(self):
        for _ in range(10):
            time.sleep(0.5)
            self.produce()

# -----------------------------
# Main Function
# -----------------------------
def main():
    producer = Producer(name="Producer")
    consumer = Consumer(name="Consumer")

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()
    logging.info("Producer-Consumer with Factorial completed!")

# -----------------------------
# Entry Point
# -----------------------------
if __name__ == "__main__":
    main()

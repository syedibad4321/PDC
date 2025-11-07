import logging
import threading
import time
import random
import os

# -----------------------------
# Logging Setup
# -----------------------------
LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# -----------------------------
# Shared Resources
# -----------------------------
semaphore = threading.Semaphore(0)
number_for_factorial = 0
results = []

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
def consumer():
    global number_for_factorial
    logging.info("Consumer waiting for number")
    semaphore.acquire()  # wait until a number is produced
    result = factorial(number_for_factorial)
    logging.info(f"Consumer calculated factorial of {number_for_factorial} = {result}, PID={os.getpid()}")
    results.append((number_for_factorial, result))

# -----------------------------
# Producer Thread
# -----------------------------
def producer():
    global number_for_factorial
    time.sleep(random.randint(1,3))  # simulate delay
    number_for_factorial = random.randint(3, 10)  # produce a number
    logging.info(f"Producer produced number {number_for_factorial}, PID={os.getpid()}")
    semaphore.release()  # signal consumer

# -----------------------------
# Main Function
# -----------------------------
def main():
    global results
    for i in range(5):  # run 5 cycles
        t_consumer = threading.Thread(target=consumer, name=f"Consumer#{i+1}")
        t_producer = threading.Thread(target=producer, name=f"Producer#{i+1}")

        t_consumer.start()
        t_producer.start()

        t_consumer.join()
        t_producer.join()

    logging.info("All factorials calculated:")
    for num, res in results:
        logging.info(f"Factorial of {num} = {res}")

# -----------------------------
# Entry Point
# -----------------------------
if __name__ == "__main__":
    main()

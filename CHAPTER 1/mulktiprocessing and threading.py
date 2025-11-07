import time
import threading
import multiprocessing
import random

NUM_WORKERS = 10
size = 1_000_000  # reduced size for demonstration


# 🔹 worker function
def do_something(count, out_list):
    for _ in range(count):
        out_list.append(random.random())


if __name__ == "__main__":

    # =========================
    # Serial execution
    # =========================
    out_list = []
    start_time = time.time()
    for _ in range(NUM_WORKERS):
        do_something(size, out_list)
    end_time = time.time()
    print("Serial time =", end_time - start_time, "seconds")


    # =========================
    # MultiThreading
    # =========================
    out_list = []
    jobs = []
    for i in range(NUM_WORKERS):
        # ✅ pass function reference, not call
        thread = threading.Thread(target=do_something, args=(size, out_list))
        jobs.append(thread)

    start_time = time.time()
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    end_time = time.time()
    print("Threading time =", end_time - start_time, "seconds")


    # =========================
    # MultiProcessing
    # =========================
    manager = multiprocessing.Manager()
    out_list = manager.list()  # shared list between processes
    jobs = []
    for i in range(NUM_WORKERS):
        process = multiprocessing.Process(target=do_something, args=(size, out_list))
        jobs.append(process)

    start_time = time.time()
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    end_time = time.time()
    print("Multiprocessing time =", end_time - start_time, "seconds")

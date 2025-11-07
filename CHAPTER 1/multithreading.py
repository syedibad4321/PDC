# ======================================
# FACTORIAL PROGRAM (with MULTITHREADING)
# ======================================

import time
import threading


# 🔹 function jo heavy kaam karega (jaise factorial)
def do_something(size, out_list):
    """Simulate heavy work — factorial-like computation"""
    for i in range(size):
        out_list.append(i * i)  # simple dummy computation


if __name__ == "__main__":
    start_time = time.time()
    size = 1_000_000     # workload
    threads = 10         # number of threads
    jobs = []

    for i in range(threads):
        out_list = []
        # ❌ tumhare code me ye galti thi: target=do_something(size, out_list)
        # ✅ correct version: target=do_something, args=(size, out_list)
        thread = threading.Thread(target=do_something, args=(size, out_list))
        jobs.append(thread)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    print("List processing complete.")
    end_time = time.time()
    print("Multithreading time =", end_time - start_time, "seconds")

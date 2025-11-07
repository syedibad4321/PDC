from mpi4py import MPI
import numpy as np
import time
import os

# -----------------------------
# Factorial Function
# -----------------------------
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        time.sleep(0.1)  # simulate computation
    return result

# -----------------------------
# MPI Initialization
# -----------------------------
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# -----------------------------
# Each process creates an array of numbers
# -----------------------------
senddata = (rank + 1) * np.arange(size, dtype=int)
recvdata = np.empty(size, dtype=int)

# -----------------------------
# All-to-All Communication
# -----------------------------
comm.Alltoall([senddata, MPI.INT], [recvdata, MPI.INT])

# -----------------------------
# Calculate factorial of received numbers
# -----------------------------
factorials = [factorial(n) for n in recvdata]

# -----------------------------
# Print results
# -----------------------------
print(f"Process {rank}: sending {senddata}, receiving {recvdata}, factorials {factorials}")

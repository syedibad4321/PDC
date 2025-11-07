from mpi4py import MPI
import time
import os

# -----------------------------
# Factorial Function
# -----------------------------
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        time.sleep(0.1)  # simulate computation
    return result

# -----------------------------
# MPI Initialization
# -----------------------------
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# -----------------------------
# Broadcast a number from root (process 0)
# -----------------------------
if rank == 0:
    variable_to_share = 7  # number to broadcast
else:
    variable_to_share = None

variable_to_share = comm.bcast(variable_to_share, root=0)

# -----------------------------
# Each process calculates factorial of received number
# -----------------------------
fact = factorial(variable_to_share)

# -----------------------------
# Print results
# -----------------------------
print(f"Process {rank} received {variable_to_share}, factorial = {fact}, PID={os.getpid()}")

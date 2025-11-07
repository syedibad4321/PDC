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
        time.sleep(0.05)  # simulate computation
    return result

# -----------------------------
# MPI Initialization
# -----------------------------
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# -----------------------------
# Scatter array from root (process 0)
# -----------------------------
if rank == 0:
    array_to_share = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
else:
    array_to_share = None

# Each process will receive one element (assuming size <= len(array))
recvbuf = comm.scatter(array_to_share, root=0)

# -----------------------------
# Factorial computation
# -----------------------------
fact = factorial(recvbuf)

# -----------------------------
# Print results
# -----------------------------
print(f"Process {rank}, PID={os.getpid()} received {recvbuf}, factorial = {fact}")

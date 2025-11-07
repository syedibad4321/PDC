from mpi4py import MPI
import time
import os

# -----------------------------
# Factorial Function
# -----------------------------
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        time.sleep(0.001)  # simulate work
    return result

# -----------------------------
# MPI Initialization
# -----------------------------
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

print(f"My rank is: {rank}, PID={os.getpid()}")

# -----------------------------
# Process 0 sends a number to process 4
# -----------------------------
if rank == 0:
    data = 10  # example smaller number for demo
    destination_process = 4
    comm.send(data, dest=destination_process)
    print(f"Process {rank} sending data {data} to process {destination_process}")

# -----------------------------
# Process 1 sends string to process 8
# -----------------------------
if rank == 1:
    data = "hello"
    destination_process = 8
    comm.send(data, dest=destination_process)
    print(f"Process {rank} sending data '{data}' to process {destination_process}")

# -----------------------------
# Process 4 receives number from process 0 and calculates factorial
# -----------------------------
if rank == 4:
    data = comm.recv(source=0)
    print(f"Process {rank} received data = {data}")
    if isinstance(data, int):
        fact = factorial(data)
        print(f"Process {rank} factorial of {data} = {fact}")

# -----------------------------
# Process 8 receives string from process 1 and calculates factorial of length
# -----------------------------
if rank == 8:
    data1 = comm.recv(source=1)
    print(f"Process {rank} received data = {data1}")
    if isinstance(data1, str):
        length = len(data1)
        fact = factorial(length)
        print(f"Process {rank} factorial of length {length} = {fact}")

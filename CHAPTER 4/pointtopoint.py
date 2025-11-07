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
        time.sleep(0.1)  # simulate computation
    return result

# -----------------------------
# MPI Initialization
# -----------------------------
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# -----------------------------
# Process 1 and Process 5 exchange numbers
# -----------------------------
if rank == 1:
    data_send = 6  # number to send
    destination_process = 5
    source_process = 5

    # Receive first (to avoid deadlock)
    data_received = comm.recv(source=source_process)
    comm.send(data_send, dest=destination_process)

    print(f"Process {rank} sent {data_send} to process {destination_process}")
    print(f"Process {rank} received {data_received} from process {source_process}")

    # Calculate factorial of received number
    fact = factorial(data_received)
    print(f"Process {rank} factorial of received number {data_received} = {fact}")

if rank == 5:
    data_send = 4  # number to send
    destination_process = 1
    source_process = 1

    comm.send(data_send, dest=destination_process)
    data_received = comm.recv(source=source_process)

    print(f"Process {rank} sent {data_send} to process {destination_process}")
    print(f"Process {rank} received {data_received} from process {source_process}")

    # Calculate factorial of received number
    fact = factorial(data_received)
    print(f"Process {rank} factorial of received number {data_received} = {fact}")

"# PDC" 

This repository contains Python implementations of core Parallel and Distributed Computing concepts. It covers multithreading, multiprocessing, thread synchronization, MPI, AsyncIO, and Distributed Task Queues (Celery).

## 📂 Repository Structure

### Chapter 1 – Threading & Multiprocessing
Focuses on the basics of creating threads and processes, along with safety mechanisms.
- **Multithreading & Multiprocessing:** Basic implementation examples.
- **Factorial Calculation:** Implemented using various synchronization primitives:
  - `Threading`
  - `RLock` (Reentrant Lock)
  - `Condition` Variables
  - `Semaphore`
- **Producer-Consumer Problem:** Solved using threads.
- **Thread Safety:** Demonstrations using `Lock` and `RLock`.

### Chapter 2 – Thread Synchronization
Advanced synchronization techniques to manage concurrent operations.
- **Barrier:** Coordinating multiple threads to wait for each other.
- **Queue:** Implementing thread-safe data sharing.
- **Semaphore:** Controlling access to a limited number of resources.
- **Thread-Safe Factorial:** performing calculations safely across multiple threads.

### Chapter 3 – Process-Based Parallelism
Explores parallelism using separate memory spaces (Processes) instead of threads.
- **Inter-Process Communication (IPC):**
  - **Pipes:** For two-way communication between processes.
  - **Queues:** For producer-consumer models in multiprocessing.
- **Process Management:**
  - Daemon vs. Non-Daemon processes.
  - Spawning processes with custom functions.
- **Parallel Computation:** Factorial and other math computations using multiple processes.

### Chapter 4 – MPI (Message Passing Interface)
- Examples using `mpi4py` library:
  - **All-to-All communication**
  - **Scatter & Gather**
  - **Broadcast**
  - **Send & Receive**
- Factorial calculations and data sharing across processes using MPI.

---

## How to Run
1. Clone the repository:

```bash
pip install mpi4py celery
# PDC - Parallel & Distributed Computing

This repository contains Python implementations of core Parallel and Distributed Computing concepts. It covers multithreading, multiprocessing, thread synchronization, MPI, AsyncIO, and Distributed Task Queues (Celery).

## 📂 Repository Structure

### Chapter 1 – Threading & Multiprocessing
Focuses on the basics of creating threads and processes, along with safety mechanisms.
- **Multithreading & Multiprocessing:** Basic implementation examples.
- **Factorial Calculation:** Implemented using various synchronization primitives:
  - Threading
  - RLock (Reentrant Lock)
  - Condition Variables
  - Semaphore
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
Distributed computing examples using the `mpi4py` library.
- **Collective Communication:**
  - All-to-All communication
  - Scatter & Gather
  - Broadcast
- **Point-to-Point:** Send & Receive
- **Applications:** Factorial calculations and data sharing across processes using MPI.

### Chapter 5 – AsyncIO & Concurrency
Asynchronous programming and concurrent execution using Python's modern libraries.
- **AsyncIO:**
  - Understanding **Event Loops** and **Coroutines**.
  - Managing **Tasks** and **Futures** for non-blocking execution.
- **Concurrent Futures:**
  - Using **Pooling** mechanisms for efficient execution of multiple tasks.

### Chapter 6 – Distributed Tasks & Socket Programming
Distributed task queues and network programming concepts.
- **Celery (Distributed Tasks):**
  - Setting up Celery workers with a broker (RabbitMQ/Redis).
  - Offloading background tasks to workers.
- **Socket Programming:**
  - **Simple Server:** Basic socket connection setup.
  - **Chain Topology:** Implementing a multi-node network (Client → Middle Node → Final Server).

---

## 🚀 How to Run

### 1. Prerequisites
Install the required libraries:
```bash
pip install mpi4py celery

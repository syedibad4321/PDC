# PDC - Parallel & Distributed Computing

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
Distributed computing examples using the `mpi4py` library.
- **Point-to-Point Communication:** `Send` and `Receive`.
- **Collective Communication:**
  - **Broadcast:** Sending data from one node to all.
  - **Scatter & Gather:** Distributing tasks and collecting results.
  - **All-to-All:** Complex data exchange patterns.
- **MPI Applications:** Factorial calculations and data sharing across distributed processes.

### Chapter 5 – AsyncIO & Concurrency
Asynchronous programming and concurrent execution using Python's modern libraries.
- **AsyncIO:**
  - Understanding **Event Loops** and **Coroutines**.
  - Managing **Tasks** and **Futures**.
  - Asynchronous execution flow.
- **Concurrent Futures:**
  - Using **Pooling** mechanisms for efficient execution.

### Chapter 6 – Celery & Socket Programming
Distributed task queues and network programming concepts.
- **Celery (Distributed Tasks):**
  - Setting up Celery workers.
  - Running background tasks.
- **Socket Programming:**
  - **Simple Server:** Basic socket connection setup.
  - **Chain Topology:** Implementing a multi-node network (Client → Middle Node → Final Server).

---

## 🛠️ Prerequisites

To run the examples in this repository, you need Python installed along with the required libraries.

```bash
pip install mpi4py celery
"# PDC" 

---

## Chapter Details

### Chapter 1 – Threading & Multiprocessing
- **Multithreading and multiprocessing** examples in Python.
- **Factorial calculation** using:
  - Threading
  - RLock
  - Condition
  - Semaphore
- **Producer-Consumer** examples implemented in threads.
- Demonstrates thread safety using `Lock` and `RLock`.

---

### Chapter 2 – Thread Synchronization
- Examples using:
  - **Barrier** for thread coordination.
  - **Queue** for thread-safe data sharing.
  - **Semaphore** for controlling access to shared resources.
- Demonstrates **thread-safe factorial calculations** using these synchronization primitives.

---

### Chapter 3 – Process-Based Parallelism
- **Multiprocessing** examples:
  - Pipes for communication between processes.
  - Queue-based producer-consumer.
  - Daemon vs non-daemon processes.
  - Spawn processes with custom functions.
- Factorial and other computations parallelized using **processes**.

---

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
git clone https://github.com/syedibad4321/PDC.git
cd PDC

import concurrent.futures
import time

number_list = list(range(1, 11))

def count(number):
    for i in range(0, 10000000):
        i += 1
    return i * number

def evaluate(item):
    start = time.perf_counter()
    result_item = count(item)
    end = time.perf_counter()
    print(f'Item {item}, result {result_item}, Duration: {end - start:.2f}s')
    return result_item

if __name__ == '__main__':
    print("\n--- Sequential Execution ---")
    start_time = time.perf_counter()
    results_seq = []
    for item in number_list:
        results_seq.append(evaluate(item))
    print(f'Sequential Execution Total Time: {time.perf_counter() - start_time:.2f}s')

    print("\n--- Thread Pool Execution ---")
    start_time = time.perf_counter()
    results_thread = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(evaluate, item) for item in number_list]
        for future in concurrent.futures.as_completed(futures):
            results_thread.append(future.result())
    print(f'Thread Pool Execution Total Time: {time.perf_counter() - start_time:.2f}s')

    print("\n--- Process Pool Execution ---")
    start_time = time.perf_counter()
    results_process = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(evaluate, item) for item in number_list]
        for future in concurrent.futures.as_completed(futures):
            results_process.append(future.result())
    print(f'Process Pool Execution Total Time: {time.perf_counter() - start_time:.2f}s')

import multiprocessing

# -----------------------------
# Factorial Function
# -----------------------------
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# -----------------------------
# Producer Process
# -----------------------------
def create_numbers(pipe):
    output_pipe, _ = pipe
    for number in range(5, 10):  # numbers for factorial
        output_pipe.send(number)
    output_pipe.close()

# -----------------------------
# Consumer Process
# -----------------------------
def calculate_factorial(pipe_in, pipe_out):
    pipe_in_close, input_pipe = pipe_in
    pipe_in_close.close()
    output_pipe, _ = pipe_out
    try:
        while True:
            number = input_pipe.recv()
            result = factorial(number)
            output_pipe.send((number, result))
    except EOFError:
        output_pipe.close()

# -----------------------------
# Main Function
# -----------------------------
if __name__ == "__main__":
    # Pipe 1: Producer -> Factorial Process
    pipe_1 = multiprocessing.Pipe(True)
    producer_process = multiprocessing.Process(target=create_numbers, args=(pipe_1,))
    producer_process.start()

    # Pipe 2: Factorial Process -> Main Process
    pipe_2 = multiprocessing.Pipe(True)
    factorial_process = multiprocessing.Process(target=calculate_factorial, args=(pipe_1, pipe_2))
    factorial_process.start()

    # Close unused ends in main process
    pipe_1[0].close()
    pipe_2[0].close()

    # Receive and print results
    try:
        while True:
            number, result = pipe_2[1].recv()
            print(f"Factorial of {number} = {result}")
    except EOFError:
        print("End of factorial calculation.")

    producer_process.join()
    factorial_process.join()

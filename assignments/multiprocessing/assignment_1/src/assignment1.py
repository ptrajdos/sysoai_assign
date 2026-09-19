import multiprocessing as mp
import random
import time


def worker(n_points, inside, lock):
    local_inside = 0

    for _ in range(n_points):
        x = random.random()
        y = random.random()

        if x * x + y * y <= 1.0:
            local_inside += 1

    #TODO uzupełnić


def main():
    n_processes = 4
    n_points_per_process = 1_000_000

    
    processes = []

    start = time.perf_counter()

    for _ in range(n_processes):
        process = mp.Process(
            target=worker,
            #TODO uzupełnić
        )
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    elapsed = time.perf_counter() - start

    total = n_processes * n_points_per_process
    inside = None
    pi = 4.0 * inside / total

    print(f"Processes: {n_processes}")
    print(f"Points:    {total:,}")
    print(f"Inside:    {inside.value:,}")
    print(f"Pi:        {pi:.8f}")
    print(f"Time:      {elapsed:.3f} s")


if __name__ == "__main__":
    main()
import multiprocessing as mp
import math
import time

import matplotlib.pyplot as plt
import numpy as np


def worker(start, end, window, signal, result):
    half = window // 2

    #TODO uzupełnić


def moving_average_parallel(signal, window, n_processes):
    n = len(signal)

    shared_signal = None
    result = None

    processes = []
    chunk_size = math.ceil(n / n_processes)

    for process_id in range(n_processes):
        start = process_id * chunk_size
        end = min(start + chunk_size, n)

        if start >= n:
            break

        process = mp.Process(
            target=worker,
            args=(start, end, window, shared_signal, result),
        )
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    return np.frombuffer(result, dtype=np.float64).copy()


def main():
    n = 20_000
    sample_rate = 1_000
    window = 101
    n_processes = 4

    rng = np.random.default_rng(42)

    t = np.arange(n) / sample_rate

    # Clean signal + Gaussian noise.
    clean = (
        np.sin(2 * np.pi * 5 * t)
        + 0.5 * np.sin(2 * np.pi * 17 * t)
    )
    noise = rng.normal(0, 0.7, size=n)
    signal = clean + noise

    start = time.perf_counter()

    filtered = moving_average_parallel(
        signal,
        window,
        n_processes,
    )

    elapsed = time.perf_counter() - start

    print(f"Samples:   {n:,}")
    print(f"Window:    {window}")
    print(f"Processes: {n_processes}")
    print(f"Time:      {elapsed:.3f} s")

    # Plot a shorter section so the filtering effect is visible.
    plot_samples = 3_000

    plt.figure(figsize=(12, 5))
    plt.plot(t[:plot_samples], signal[:plot_samples], label="Noisy signal")
    plt.plot(
        t[:plot_samples],
        filtered[:plot_samples],
        label="Moving average",
        linewidth=2,
    )
    plt.plot(
        t[:plot_samples],
        clean[:plot_samples],
        label="Original clean signal",
        linewidth=1,
    )

    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.title("Parallel moving-average filter")
    plt.legend()
    plt.tight_layout()
    plt.savefig("moving_average.png", dpi=150)
    plt.close()

    print("Saved: moving_average.png")


if __name__ == "__main__":
    main()

import threading as th
from sklearn.datasets import make_classification
import pandas as pd
import os
from tools.paths import path
import time


def file_processing_sequential(file_path, results: dict):
    data = pd.read_csv(file_path)
    means = data.mean()
    results[file_path] = means.to_dict()


def sequential_processing(file_directory):
    results = {}
    start_time = time.time()
    for file_name in os.listdir(file_directory):
        file_path = os.path.join(file_directory, file_name)
        if os.path.isfile(file_path) and file_name.endswith(".csv"):
            file_processing_sequential(file_path, results)
    end_time = time.time()
    print(f"Sequential processing time: {end_time - start_time}")
    return results


def file_processing_threaded(file_path, results: dict, lock: th.Lock):
    raise NotImplementedError(
        "You need to implement the file_processing_threaded function to process a single CSV file and store the results in a shared dictionary."
    )


def threaded_processing(file_directory, num_threads=5):
    results = {}
    lock = th.Lock()
    start_time = time.time()
    threads = []
    file_list = [
        f
        for f in os.listdir(file_directory)
        if os.path.isfile(os.path.join(file_directory, f)) and f.endswith(".csv")
    ]
    file_chunks = None

    raise NotImplementedError(
        "You need to implement the logic to divide the file_list into chunks for threading."
    )

    end_time = time.time()
    print(f"Threaded processing time: {end_time - start_time}")
    return results


def main():
    data_dir = path("data", "root")
    dataset_location = os.path.join(data_dir, "threading", "assignment_1")
    results = sequential_processing(dataset_location)
    threaded_results = threaded_processing(dataset_location, num_threads=2)


if __name__ == "__main__":
    main()

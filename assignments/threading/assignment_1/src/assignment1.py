import threading as th
from sklearn.datasets import make_classification
import pandas as pd
import os
from tools.paths import path

class DataGenerator(th.Thread):

    def __init__(self, make_classification_options: dict, file_path: str) -> None:
        super().__init__()
        self.make_classification_options = make_classification_options
        self.file_path = file_path

    def run(self) -> None:

        X, y = make_classification(**self.make_classification_options)
        df = pd.DataFrame(X)
        df['target'] = y
        df.to_csv(self.file_path, index=False)


def main():
    make_classification_options = {
        'n_samples': 1000,
        'n_features': 20,
        'n_informative': 15,
        'n_redundant': 5,
    }
    data_dir = path('data', 'root')
    dataset_location = os.path.join(data_dir, 'threading', 'assignment_1')
    os.makedirs(dataset_location, exist_ok=True)
    N = 5
    threads = []  
    for i in range(N):
        file_name = f'synthetic_data_{i}.csv'
        file_path = os.path.join(dataset_location, file_name)
        make_classification_options['random_state'] = i

        data_generator = DataGenerator(make_classification_options, file_path)

        data_generator.start()
        threads.append(data_generator)

    for t in threads:
        t.join()
        
if __name__ == "__main__":
    main()
import multiprocessing as mp
import time
import random

#TODO finish it.

def reader(reader_id, data, condition, active_readers):
    for _ in range(5):
        with condition:
            while data["writer"]:
                condition.wait()

            active_readers.value += 1

        # Reading does not require exclusive access.
        print(
            f"Reader {reader_id}: value={data['value']}",
            flush=True,
        )
        time.sleep(random.uniform(0.1, 0.4))

        with condition:
            active_readers.value -= 1

            if active_readers.value == 0:
                condition.notify_all()

        time.sleep(random.uniform(0.1, 0.5))


def writer(writer_id, data, condition, active_readers):
    for _ in range(5):
        with condition:
            while data["writer"] or active_readers.value > 0:
                condition.wait()

            data["writer"] = True

        # Exclusive writing section.
        old_value = data["value"]
        time.sleep(random.uniform(0.1, 0.3))
        data["value"] = old_value + 1

        print(
            f"Writer {writer_id}: value={data['value']}",
            flush=True,
        )

        with condition:
            data["writer"] = False
            condition.notify_all()

        time.sleep(random.uniform(0.1, 0.5))


def main():
    manager = mp.Manager()

    data = manager.dict({
        "value": 0,
        "writer": False,
    })

    condition = mp.Condition()
    active_readers = mp.Value("i", 0)

    processes = []

    for i in range(4):
        processes.append(
            mp.Process(
                target=reader,
                args=(i, data, condition, active_readers),
            )
        )

    for i in range(2):
        processes.append(
            mp.Process(
                target=writer,
                args=(i, data, condition, active_readers),
            )
        )

    for p in processes:
        p.start()

    for p in processes:
        p.join()


if __name__ == "__main__":
    main()
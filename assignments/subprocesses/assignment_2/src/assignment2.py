import subprocess


def guess_number():
    process = subprocess.Popen(
    ) #TODO uzupełnić

    # Wait for the C program to become ready.
    response = process.stdout.readline().strip()

    if response != "READY":
        raise RuntimeError(f"Unexpected response: {response!r}")

    low = 0
    high = 100
    attempts = 0

    while low <= high:
        guess = (low + high) // 2
        attempts += 1

        print(f"Python: sending {guess}")

        #TODO wysłać wiadomość

        response = process.stdout.readline().strip()

        print(f"C: {response}")

        if response == "CORRECT":
            print(f"Found {guess} in {attempts} attempts")
            break

        elif response == "TOO_LOW":
            low = guess + 1

        elif response == "TOO_HIGH":
            high = guess - 1

        else:
            raise RuntimeError(f"Unexpected response: {response!r}")

    process.stdin.close()
    process.wait()


if __name__ == "__main__":
    guess_number()
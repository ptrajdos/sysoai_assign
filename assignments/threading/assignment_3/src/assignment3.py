import random
import threading
import time


class Bank:
    def __init__(self, n_accounts, initial_balance):
    
        self._accounts = {
            f"Account-{i:02d}": initial_balance for i in range(n_accounts)
        }

        self._reserve = 0

        self._initial_total = self._total_balance()

    def deposit(self, account, amount):
        
        balance = self._accounts[account]

        time.sleep(0.0001)

        self._accounts[account] = balance + amount
        self._reserve -= amount

    def withdraw(self, account, amount):
        
        balance = self._accounts[account]

        if balance < amount:
            return False

        current = balance

        time.sleep(0.0001)

        self._accounts[account] = current - amount
        self._reserve += amount

        return True

    def transfer(self, source, destination, amount):
        if self.withdraw(source, amount):
            self.deposit(destination, amount)
            return True

        return False

    def _total_balance(self):
        return sum(self._accounts.values()) + self._reserve

    def total_balance(self):
        
        return self._total_balance()

    def account_names(self):
        
        return list(self._accounts)

    def accounts(self):
        
        return dict(self._accounts)

    def check_integrity(self):
        
        total = self._total_balance()

        if total != self._initial_total:
            raise RuntimeError(
                "Bank integrity check failed: "
                f"expected {self._initial_total}, "
                f"got {total}"
            )

        if any(balance < 0 for balance in self._accounts.values()):
            raise RuntimeError(
                "Bank integrity check failed: " "negative account balance"
            )

        return True


def worker(bank, operations):
    thread_name = threading.current_thread().name
    accounts = bank.account_names()

    for _ in range(operations):
        operation = random.choice(("deposit", "withdraw", "transfer"))

        source = random.choice(accounts)
        amount = random.randint(1, 10)

        if operation == "deposit":
            bank.deposit(source, amount)

            print(
                f"[{thread_name}] " f"deposit {amount:2d} -> {source}",
                flush=True,
            )

        elif operation == "withdraw":
            success = bank.withdraw(source, amount)

            print(
                f"[{thread_name}] "
                f"withdraw {amount:2d} <- {source} "
                f"{'OK' if success else 'FAILED'}",
                flush=True,
            )

        else:
            destination = random.choice(accounts)

            if source == destination:
                continue

            success = bank.transfer(
                source,
                destination,
                amount,
            )

            print(
                f"[{thread_name}] "
                f"transfer {amount:2d} "
                f"{source} -> {destination} "
                f"{'OK' if success else 'FAILED'}",
                flush=True,
            )


def main():
    bank = Bank(
        n_accounts=10,
        initial_balance=1_000,
    )

    threads = [
        threading.Thread(
            target=worker,
            args=(bank, 100),
            name=f"Worker-{i:02d}",
        )
        for i in range(10)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    bank.check_integrity()

    print("\nFinal balances:")

    for account, balance in bank.accounts().items():
        print(f"  {account}: {balance}")

    print(f"  Bank reserve: {bank._reserve}")
    print(f"\nTotal: {bank.total_balance()}")
    print("SANITY CHECK PASSED")


if __name__ == "__main__":
    main()

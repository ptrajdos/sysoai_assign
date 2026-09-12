import random
import threading
import time


class MagicStatue:
    def __init__(self, number_of_mages):
        self.number_of_mages = number_of_mages
        self.touched_by = set()
        self.lock = threading.Lock()
        self.game_over = False
        self.turn = -1

    def setup_turn(self):

        with self.lock:
            if self.game_over:
                return

            self.turn += 1
            self.touched_by.clear()

            print(f"Statue prepared for turn {self.turn}")

    def touch(self, mage_id):
        with self.lock:
            if self.game_over:
                return

            self.touched_by.add(mage_id)

    def complete_ritual(self):

        with self.lock:
            if self.game_over:
                return

            if not self.touched_by:
                return

            if len(self.touched_by) == self.number_of_mages:
                print(f"Turn {self.turn}: ritual succeeds!")
                self.touched_by.clear()
                return

            print("BOOM! The statue explodes. Game over.")
            self.game_over = True


class Mage(threading.Thread):
    def __init__(self, mage_id, statue, turns):
        super().__init__(name=f"Mage-{mage_id}")
        self.mage_id = mage_id
        self.statue = statue
        self.turns = turns

    def run(self):
        for turn in range(self.turns):
            if self.statue.game_over:
                return

            if self.mage_id == 0:
                self.statue.setup_turn()

            time.sleep(random.uniform(0.01, 0.1))
            self.statue.touch(self.mage_id)

            if self.mage_id == 0:
                self.statue.complete_ritual()


class Simulation:
    def __init__(self, number_of_mages, number_of_turns):
        self.statue = MagicStatue(number_of_mages)

        self.mages = [
            Mage(
                mage_id=i,
                statue=self.statue,
                turns=number_of_turns,
            )
            for i in range(number_of_mages)
        ]

    def run(self):

        for mage in self.mages:
            mage.start()

        for mage in self.mages:
            mage.join()

        assert not self.statue.game_over, "The ritual failed. The statue exploded."


def main():
    simulation = Simulation(
        number_of_mages=5,
        number_of_turns=10,
    )

    simulation.run()


if __name__ == "__main__":
    main()

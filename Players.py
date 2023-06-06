from abc import abstractmethod


class Player:
    def __init__(self, value: str, board):
        self.value = value
        self.board = board

    @abstractmethod
    def move(self):
        while True:
            number = input("Choose board coars from 1-9 -> ")
            if number.isdigit():
                number = int(number)
            else:
                print("Type integer from 1-9")
                continue
            if number not in self.board.get_free_slots():
                print(
                    f"Please choose a free slot from {self.board.get_free_slots()}")
                continue

            break
        print("number=", number)
        self.board.change_board_state(number, self.value)

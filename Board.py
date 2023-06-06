class BoardClass:
    def __init__(self):
        self.board_state = ["*", "*", "*", "*", "*", "*", "*", "*", "*"]

    def change_board_state(self, number: int, string: str):
        self.board_state[number-1] = string

    def print_board(self):
        for i in range(3):
            for j in range(3):
                print(self.board_state[i*3+j], end=" ")
            print()

    def get_free_slots(self):
        free_slots = []
        for index, value in enumerate(self.board_state):
            if value == "*":
                free_slots.append(index+1)
        return free_slots


if __name__ == "__main__":
    b = BoardClass()
    b.change_board_state(3, "x")
    b.change_board_state(1, "o")
    b.print_board()
    print(b.get_free_slots())

from Board import BoardClass
from HumanPlayer import HumanPlayer
from CompPlayer import CompPlayer


class Game:
    def __init__(self):
        self.board = BoardClass()
        self.human = HumanPlayer("x", self.board)
        self.comp = CompPlayer("o", self.board)

    def play(self):
        while True:
            self.human.move()
            self.board.print_board()
            if self.check(self.human):
                break
            self.comp.move()
            self.board.print_board()
            if self.check(self.comp):
                break

    def check(self, player) -> bool:
        board_state = self.board.board_state
        for i in range(3):
            if board_state[i*3: (i+1)*3] == [player.value]*3:
                print(player.value, "You win!")
                return True
            if [board_state[i], board_state[i+3], board_state[i+6]] == [player.value]*3:
                print(player.value, "You win!")
                return True
            if [board_state[0], board_state[4], board_state[8]] == [player.value]*3:
                print(player.value, "You win!")
                return True
            if [board_state[2], board_state[4], board_state[6]] == [player.value]*3:
                print(player.value, "You win!")
                return True
            if len(self.board.get_free_slots()) == 0:
                print("Start a new game")
                return True
            return False


if __name__ == "__main__":
    game = Game()
    game.play()

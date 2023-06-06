import random
from Players import Player


class CompPlayer(Player):
    def move(self):

        number = random.choice(self.board.get_free_slots())
        print("number=", number)
        self.board.change_board_state(number, self.value)

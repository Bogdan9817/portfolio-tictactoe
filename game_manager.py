import numpy as np


PLAYER_ONE = [0,0,0]
PLAYER_TWO = [1,1,1]

class GameManager:
    def __init__(self):
        self.turn = True
        self.over = False
        self.winner = None
        self.game_field = np.empty((3,3))
    def switch_turn(self):
        self.turn = not self.turn
    def check_field(self):
        for n in self.game_field:
            self.is_match(n)
        for n in np.transpose(self.game_field):
            self.is_match(n)

        self.is_match(np.diag(self.game_field))
        self.is_match(np.diag(np.flipud(self.game_field)))
        if np.all((self.game_field == 0) | (self.game_field == 1)):
            self.over = True
            self.winner = "Draw"
    def is_match(self, to_compare):
        if self.over:
            return
        elif np.array_equal(to_compare, PLAYER_TWO) or np.array_equal(to_compare, PLAYER_ONE):
            self.over = True
            self.winner = "Player 1" if np.array_equal(to_compare, PLAYER_ONE) else "Player 2"
    def make_turn(self, pos):
        if self.over:
            return
        if self.game_field[pos[0]][pos[1]] == 1 or self.game_field[pos[0]][pos[1]] == 0:
            return "USED CELL"
        self.game_field[pos[0]][pos[1]] = 0 if self.turn else 1
        self.check_field()
        self.switch_turn()
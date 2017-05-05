import random


class Player:
    """Player class for Tic-Tac-Toe. Randomly moves on the board for a valid space"""

    def __init__(self, player_num):
        self.player_num = player_num

    @staticmethod
    def get_move(board):
        """Pretend it is a player that gives a random move within the board"""
        x_rand = random.randrange(len(board))
        y_rand = random.randrange(len(board[0]))
        return x_rand, y_rand

    def __repr__(self):
        return 'Player %s' % self.player_num

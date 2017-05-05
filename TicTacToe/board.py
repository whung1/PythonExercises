import numpy as np


class Board:

    def __init__(self, x=3, y=3):
        self.board = np.zeros((x, y))
        self.free_spaces = x * y

    def insert_move(self, player_num, coords):
        if self.board[coords[0], coords[1]] == 0:
            self.board[coords[0], coords[1]] = player_num
            self.free_spaces -= 1
            return True  # Space was empty and player piece is inserted here now
        else:
            return False  # another player_num has a piece here

    def is_full(self):
        if self.free_spaces == 0:
            return True
        else:
            return False

    def check_win(self, player_num):
        """Checks every row and column for matching, along with two diagonals towards upper right and bottom right"""
        horizontal_checks = self.check_horizontal_win(player_num)
        vertical_checks = self.check_vertical_win(player_num)
        diagonal_ur_check = self.check_diagonal_win(player_num, 0, 0, 1, 1)
        diagonal_br_check = self.check_diagonal_win(player_num, 0, len(self.board)-1, 1, -1)
        return horizontal_checks or vertical_checks or diagonal_br_check or diagonal_ur_check

    def check_horizontal_win(self, player_num):
        """Helper function that checks every row of the board to see
            if there is a row where every element is a player's piece for win condition"""
        for i in range(len(self.board)):
            win = True
            for j in range(len(self.board[0])):
                if self.board[i, j] != player_num:
                    win = False
                    break
            if win is True:
                return True
        return False

    def check_vertical_win(self, player_num):
        """Helper function that checks every column of the board to see
            if there is a column where every element is a player's piece for win condition"""
        for j in range(len(self.board[0])):
            win = True
            for i in range(len(self.board)):
                if self.board[i, j] != player_num:
                    win = False
                    break
            if win is True:
                return True
        return False

    def check_diagonal_win(self, player_num, x_index, y_index, x_increment, y_increment):
        """Helper function that checks diagonals based on the initial coordinate position
            and the direction of the diagonal based on increment inputs"""

        while 0 <= x_index < len(self.board) and 0 <= y_index < len(self.board[0]):
            if self.board[x_index, y_index] != player_num:
                return False
            x_index += x_increment
            y_index += y_increment
        return True

    def __str__(self):
        return str(self.board)

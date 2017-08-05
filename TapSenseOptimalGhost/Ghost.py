"""
Game of Ghost
"""
from TapSenseOptimalGhost.Trie import Trie
from TapSenseOptimalGhost.ComputerPlayer import ComputerPlayer
from TapSenseOptimalGhost.Player import Player


class GhostGame:
    def __init__(self):
        self.game_state = Trie()
        self.players = []
        self.players.append(Player("Player 1", self.game_state))
        self.players.append(ComputerPlayer("Computer 1", self.game_state))

    def execute_game(self):
        if self.is_over():
            raise ValueError

        stop = False
        while not stop:  # Game Loop
            for cur_player in self.players:
                # Get next letter / move from current player
                next_letter = None
                legal_moves = self.get_legal_moves()
                print("Legal moves: {0}".format(legal_moves))
                while next_letter not in legal_moves:
                    print("{0}'s move: ".format(cur_player.name))
                    next_letter = cur_player.get_next_move()
                    print(next_letter)
                # Move after validation
                self.execute_move(next_letter)
                # Check lose condition before next turn
                if self.is_over():
                    print("{0} loses".format(cur_player.name))
                    print("Word is {0}".format(self.game_state.cur.end))
                    self.game_state.reset()
                    # if cur_player.name == 'Computer 1':
                    #    stop = True
                    break

    # Wrapper functions for implementation of game_state
    def add_word_list(self, words):
        self.game_state.insert_words(words)

    def get_legal_moves(self):
        return self.game_state.get_next_values()

    def execute_move(self, next_letter):
        return self.game_state.traverse_to(next_letter)

    def is_over(self):
        return (self.game_state.is_leaf()
                or self.game_state.cur.distance > 5
                and self.game_state.cur.end)

    def print_over_message(self):
        (self.game_state.is_leaf()
         or self.game_state.cur.distance > 5
         and self.game_state.cur.end)


if __name__ == '__main__':
    ghost = GhostGame()
    with open('WORD_LIST_b.txt', 'r') as f:
        ghost.add_word_list(f.read().split())
    ghost.execute_game()

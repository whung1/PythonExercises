"""
Game of Ghost
"""
from Trie import Trie
from ComputerPlayer import ComputerPlayer
from Player import Player


class GhostGame:
    def __init__(self):
        self.game_state = Trie()
        self.players = []

    def execute_game(self):
        if self.is_over() or not self.players:
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
                    self.print_over_message(cur_player)
                    self.restart_round()
                    break

    # Wrapper functions for hiding implementation details of game_state
    def add_word_list(self, words):
        self.game_state.insert_words(words)

    def add_player(self, name):
        self.players.append(Player(name, self.game_state))

    def add_computer(self, name):
        self.players.append(ComputerPlayer(name, self.game_state))

    def get_legal_moves(self):
        return self.game_state.get_next_values()

    def execute_move(self, next_letter):
        return self.game_state.traverse_to(next_letter)

    def is_over(self):
        return (self.game_state.is_leaf()
                or self.game_state.cur.distance > 5
                and self.game_state.cur.end)

    def print_over_message(self, cur_player):
        if ((self.game_state.is_leaf()
             or self.game_state.cur.distance > 5)
                and self.game_state.cur.end):
            # Standard End
            print("{0} loses".format(cur_player.name))
        else:
            print("Tie")
        print("Word is {0}".format(self.game_state.cur.end))

    def restart_round(self):
        print("Restarting Round...")
        self.game_state.reset()


if __name__ == '__main__':
    ghost = GhostGame()
    print("Insert dictionary filepath:")
    with open(input(), 'r') as f:
        ghost.add_word_list(f.read().split())
    ghost.add_player('Player 1')
    ghost.add_computer('Computer 1')
    ghost.execute_game()

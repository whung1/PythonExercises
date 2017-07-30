from collections import Counter


class Player:

    def __init__(self, player_name, game_state):
        self.name = player_name
        self.game_state = game_state

    def get_next_move(self):
        return input()


class ComputerPlayer:
    def __init__(self, game_state):
        """
        :param game_state: Reference to the game state of the board
                            this ComputerPlayer will be reading from
        """
        self.game_state = game_state

    def get_next_move(self):
        """

        :param Trie of all possible words from current state
        :return Char of next move to act
        """
        # Get all possible words sorted by distance from least
        # from current location
        # O(log n)
        possible_moves = self.game_state.get_words()
        # Sort possible moves by winning and losing movies
        lose = []
        win = []
        for word_node, distance in possible_moves:
            # Even Distance = Win, Odd Distance = Lose
            if distance % 2 == 0:
                # Even
                win.append(word)
            else:
                # Odd
                lose.append(word)
        

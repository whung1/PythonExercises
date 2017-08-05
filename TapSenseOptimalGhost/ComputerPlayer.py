import random


class ComputerPlayer:
    def __init__(self, name, game_state):
        """
        :param game_state: Reference to the game state of the board
                            this ComputerPlayer will be reading from
        """
        self.name = name
        self.game_state = game_state

    def get_next_move(self):
        """
        :param Trie of all possible words from current state
        :return Char of next move to act
        """
        # Get all possible words sorted by distance from least
        # from current location, O(log n)
        possible_moves = self.calculate_next_moves()
        # Sort possible moves by winning, losing, and unknown
        winning_moves = []
        losing_moves = []
        unknown_moves = []
        for letter, values in possible_moves.items():
            move_state, distance = values
            if move_state == 1:
                winning_moves.append(letter)
            if move_state == -1:
                losing_moves.append((letter, distance))
            else:
                unknown_moves.append(letter)

        # If the computer thinks it will win, it
        # should play randomly among all its winning moves
        if winning_moves:
            return random.choice(winning_moves)
        # NOTE: No documentation for choosing when there is
        # non-losing choice, assume random
        if unknown_moves:
            return random.choice(unknown_moves)
        # If the computer thinks it will lose
        # it should play so as to extend the game as long as possible
        # (choosing randomly among choices that force the maximal
        # game length).
        maximal_distance = max(d for l, d in losing_moves)
        maximal_choices = [l for l, d in losing_moves if d == maximal_distance]
        return random.choice(maximal_choices)

    def calculate_next_moves(self):
        """
        Checks all the next possible moves and calculates whether its a
        sure win (1), unsure (0), or sure loss (-1),
        along with the max depth

        :return: Dictionary of letters as key
                    with (win_check, distance) as values
                    where win_check = 1 if win, 0 if unsure, -1 if loss
        """
        next_moves = {}
        for node in self.game_state.get_next_nodes():
            next_moves[node.val] = self.__calculate_next_move(node, 1)
        return next_moves

    def __calculate_next_move(self, node, distance):
        """
        Helper function for calculate next move.

        Traverses down DFS style to get max depth
        :param node: TrieNode
        :return: move_state, distance
        """
        # Word cannot be extended any more or if word length
        # is greater than 4 and completed = end of game
        if not node.children or node.distance > 4 and node.end:
            if node.distance > 4 and node.end:
                # Even distance = win, Odd distance = loss
                return 1 if distance % 2 == 0 else -1, distance
            else:
                # Word length is not greater than 4, will be "tie"
                return None, distance

        move_state = None
        max_distance = distance
        # Traverse through children nodes DFS
        for child in node.get_children():
            cur_state, cur_max_distance = self.__calculate_next_move(
                child, distance+1)
            max_distance = (cur_max_distance
                            if cur_max_distance > max_distance
                            else max_distance)
            move_state = (cur_state
                          if move_state is None or move_state == cur_state
                          else 0)
        return move_state, max_distance

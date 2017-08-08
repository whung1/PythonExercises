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
        # Sort possible moves by winning and losing
        winning_moves = []
        losing_moves = []
        for letter, values in possible_moves.items():
            move_state, min_d_lose = values
            if move_state == 1:
                winning_moves.append(letter)
            if move_state == -1:
                losing_moves.append((letter, min_d_lose))

        # If the computer thinks it will win, it
        # should play randomly among all its winning moves
        if winning_moves:
            return random.choice(winning_moves)
        # If the computer thinks it will lose
        # it should play so as to extend the game as long as possible
        # (choosing randomly among choices that force the maximal
        # game length).
        best_min_d = max(min_d for l, min_d in losing_moves)
        maximal_choices = [l for l, min_d in losing_moves if (
            min_d == best_min_d)]
        return random.choice(maximal_choices)

    def calculate_next_moves(self):
        """
        Checks all the next possible moves and calculates whether its a
        sure win (1) or sure loss (-1),
        along with the max depth

        :return: Dictionary of letters as key
                    with (win_check, distance) as values
                    where win_check = 1 if win and -1 if loss
        """
        next_moves = {}
        for node in self.game_state.get_next_nodes():
            next_moves[node.val] = self.__calculate_next_move(node, 1)
        print(next_moves)
        return next_moves

    def __calculate_next_move(self, node, min_d):
        """
        Helper function for calculate next move.

        Traverses down DFS style to get max depth
        :param node: TrieNode
        :return: move_state, distance
        """
        if not node.children and node.end:
            # Even distance = win, Odd distance = loss
            return 1 if min_d % 2 == 0 else -1, min_d

        move_state = None
        min_distance = None
        # Traverse through children nodes DFS
        for child in node.get_children():
            cur_state, cur_min_distance = self.__calculate_next_move(
                child, min_d+1)
            if (cur_state is -1 and
                    (min_distance is None or
                     min_distance > cur_min_distance)):
                min_distance = cur_min_distance
            # Assume optimal play, thus -1 for lose if there is any
            # path already that is a loss
            move_state = -1 if move_state == -1 else cur_state
        return move_state, min_distance

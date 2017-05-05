from collections import Counter


class Player:

    def __init__(self, player_name):
        self.current_wins = 0
        self.current_hand = Counter()  # counter of cards objects
        self.name = player_name
        self.playing = True

    def sum(self, card):
        """Add card to player's hand and then return total value of player's hand"""
        self.current_hand[card] += 1
        return self.get_score()

    def get_score(self):
        """Return the total value of a player's hand"""
        num_aces = 0
        total = 0

        for card, num in self.current_hand.items():
            if card.card_face == 'A':
                num_aces = num
            total += card.value * num

        for i in range(num_aces):  # if we have aces, calculate them last based on busting for values 1 or 11
            if total > 21:
                total -= 10
        return total

    def get_hand_str(self):
        """Return string representation of the hand's card faces"""
        if len(self.current_hand) == 0:
            return "nothing"
        card_str = ""
        for card, num in self.current_hand.items():
            card_str += "%s %s, " % (num, card.card_face)
        return card_str

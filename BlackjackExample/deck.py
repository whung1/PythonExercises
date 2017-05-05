import random


class Deck:
    def __init__(self):
        self.cards = list()
        for card_face in range(1, len(Card.card_faces)):
            for suites in range(0, 4):
                curr_card = Card(Card.card_faces[card_face], Card.card_values[card_face])
                self.cards.append(curr_card)

    def get_card(self):
        """Get a random card from the deck"""
        rand_index = random.randrange(len(self.cards))
        return self.cards.pop(rand_index)


class Card:
    """Using a class for flexibility in case of implementation of suits"""
    card_faces = [None, "A", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                  "J", "Q", "K"]
    card_values = [None, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                   10, 10, 10]

    def __init__(self, card_face, value):
        self.card_face = card_face # 2, 10, A, J, etc
        self.value = value

    def __repr__(self):
        return "<Card card_face:%s points:%s>" % (self.card_face, self.value)

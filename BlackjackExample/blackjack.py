from player import Player
from deck import Deck


class Blackjack():

    def __init__(self):
        self.players = []
        self.deck = Deck()

    def start_game(self):
        self.get_players()  # populate players for the game setup
        done = 0
        game_loop = 1
        while game_loop:
            for player in self.players:
                if player.playing:
                    choice = self.get_choice(player)
                    if choice == 'h':
                        card = self.deck.get_card()
                        print("Received a %s" % card.card_face)
                        total = player.sum(card)
                        print("Player %s has a new hand total of %s" % (player.name, total))
                        if total > 21:
                            print("Player %s has busted" % player.name)
                            player.playing = False
                            done += 1
                    elif choice == 's':
                        print("Player %s has stayed" % player.name)
                        done += 1
                    else:
                        game_loop = 0
                        break

                if done >= len(self.players):
                    game_loop = 0
                    break

        self.get_winner()

    def get_winner(self):
        winner = None
        score = 0
        for player in self.players:
            player_score = player.get_score()
            if score < player_score < 22:
                score = player_score
                winner = player
        if winner:
            print("Player %s is the winner with score of %s" % (winner.name, score))
        else:
            print("No one won")

    def get_choice(self, player):
        """Get player choice"""
        print("\nPlayer %s's turn with a hand total of %s and a hand of %s" % (player.name,
                                                                               player.get_score(),
                                                                               player.get_hand_str()))
        print("Hit (h) or Stay (s)? q to quit game")
        return input()

    def get_players(self):
        """Set up players for the game"""
        print("Number of players? 2 or above")
        num_players = int(input())
        for i in range(num_players):
            print("Player name?")
            name = input()
            self.players.append(Player(name))

if __name__ == "__main__":
    b = Blackjack()
    b.start_game()

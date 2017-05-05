from player import Player
from board import Board


def game_cycle():
    # Setup
    players = player_setup(2)
    board = Board()
    game_over = False
    winner = None

    # Begin game
    while not game_over:
        for player in players:
            print(board)        # Print board state and player turn
            print('%s\'s turn' % player)

            # Player's turn
            move_complete = False
            while not move_complete:
                player_move = player.get_move(board.board)
                move_complete = board.insert_move(player.player_num, player_move)
            print('%s\'s moved at %s' % (player, player_move))
            if board.check_win(player.player_num):  # Check win condition
                game_over = True
                winner = player
                break  # break out of player loop since game is over
            if board.is_full():  # check if board is just full
                game_over = True
                break  # break out of player loop since game is over

    # End results
    print('Winner: %s' % winner)
    print('Game over')
    print(board)


def player_setup(num_players=2):
    """Helper function to set up players"""
    players = []
    for i in range(num_players):
        players.append(Player(i+1))
    return players

if __name__ == '__main__':
    game_cycle()

import json
from field import Field
from player import Player


def main():
    [board_size, playersSymbols] = get_config()
    field = Field(board_size)
    players = [Player(symbol) for symbol in playersSymbols]
    winner = False
    player_turn = 0
    print("valid inputs: 1-" + str(board_size))
    field.print_field()
    free_indexes = field.get_free_indexes()

    while not winner and len(free_indexes) > 0:
        current_player = players[player_turn]
        if player_turn == len(players) - 1:
            winner = current_player.ai_turn(field, free_indexes)
        else:
            [row, col] = current_player.get_valid_input(field)
            winner = field.set_item(row, col, current_player.symbol)
        player_turn = (player_turn + 1) % len(players)
        field.print_field()
        free_indexes = field.get_free_indexes()

    if not winner:
        print("Game Over: TIE")
    else:
        print("Winner is: " + str(winner))


def get_config():
    with open('config.json') as config_file:
        data = json.load(config_file)
    board_size = data["boardSize"]
    playersSymbols = data["players"]
    if not Player.is_players_valid(playersSymbols) or not Field.is_board_valid(board_size):
        raise ValueError('Wrong data in config file')

    return [board_size, playersSymbols]


if __name__ == "__main__":
    main()

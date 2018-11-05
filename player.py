import random


class Player:
    ALLOWED_NUMBER_OF_PLAYERS = 3

    def __init__(self, symbol):
        self.symbol = symbol

    def get_valid_input(self, field):
        while True:
            try:
                row = int(raw_input(self.symbol + ' row: ')) - 1
                col = int(raw_input(self.symbol + ' col: ')) - 1
                if not field.is_within_grid(row, col):
                    print("Out of range")
                elif not field.is_valid_cell_free(row, col):
                    print("Cell already being used")
                else:
                    return [row, col]
            except ValueError:
                print("Invalid input")

    @staticmethod
    def is_players_valid(players_symbols):
        # Check that players don't have duplicate symbols
        return len(set(players_symbols)) == Player.ALLOWED_NUMBER_OF_PLAYERS and \
               len(players_symbols) == Player.ALLOWED_NUMBER_OF_PLAYERS

    def ai_turn(self, field, free_indexes):
        print("ai thinking...")
        random_from_free_index = random.randint(0, len(free_indexes) - 1)
        row = free_indexes[random_from_free_index][0]
        col = free_indexes[random_from_free_index][1]
        print('row: ' + str(row + 1))
        print('col: ' + str(col + 1))
        return field.set_item(row, col, self.symbol)

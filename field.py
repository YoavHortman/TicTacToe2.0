class Field:
    MIN_FIELD_SIZE = 3
    MAX_FIELD_SIZE = 10

    # None means empty spot on the grid
    def __init__(self, size):
        self.grid = [[None for row in range(size)] for col in range(size)]
        self.size = size

    # Only call this function AFTER checking if the [col][row] is empty
    # Returns if the player won
    def set_item(self, row, col, symbol):
        self.grid[row][col] = symbol
        row_winner = True
        col_winner = True
        diagonal_winner1 = True
        diagonal_winner2 = True
        for index in range(self.size):
            if self.grid[row][index] != symbol:
                row_winner = False
            if self.grid[index][col] != symbol:
                col_winner = False
            if self.grid[index][index] != symbol:
                diagonal_winner1 = False
            if self.grid[self.size - index - 1][index] != symbol:
                diagonal_winner2 = False
        if row_winner or col_winner or diagonal_winner1 or diagonal_winner2:
            return symbol
        return False

    def get_item(self, row, col):
        return self.grid[row][col]

    def get_free_indexes(self):
        free_indexes = []
        for row in range(self.size):
            for col in range(self.size):
                if self.grid[row][col] is None:
                    free_indexes.append([row, col])

        return free_indexes

    # checks if col and row are in range
    def is_within_grid(self, row, col):
        return self.size > col >= 0 and self.size > row >= 0

    # Expects a col and row in range and returns if the cell is free
    def is_valid_cell_free(self, row, col):
        return self.get_item(row, col) is None

    def print_field(self):
        for row in self.grid:
            print(row)

    @staticmethod
    def is_board_valid(board_size):
        return Field.MIN_FIELD_SIZE <= board_size <= Field.MAX_FIELD_SIZE

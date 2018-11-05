import unittest

from field import Field


class TestField(unittest.TestCase):
    def setUp(self):
        self.field = Field(3)

    def test_free_indexes_returns_all_indexes_when_empty(self):
        self.assertEqual(len(self.field.get_free_indexes()), 9)

    def test_free_indexes_returns_correct_amount_when_field_not_empty(self):
        self.field.grid[1][1] = "test"
        self.assertEqual(len(self.field.get_free_indexes()), 8)

    def test_is_within_grid_returns_false_when_out_of_grid(self):
        self.assertEqual(self.field.is_within_grid(10, 10), False)

    def test_is_within_grid_returns_true_when_in_grid(self):
        self.assertEqual(self.field.is_within_grid(1, 1), True)

    def test_is_valid_cell_free(self):
        self.assertEqual(self.field.is_valid_cell_free(2, 2), True)

    def test_is_valid_cell_not_free(self):
        self.field.grid[1][1] = "test"
        self.assertEqual(self.field.is_valid_cell_free(1, 1), False)

    def test_is_board_valid_board_too_big(self):
        self.assertEqual(Field.is_board_valid(Field.MAX_FIELD_SIZE + 1), False)

    def test_is_board_valid_board_too_small(self):
        self.assertEqual(Field.is_board_valid(Field.MIN_FIELD_SIZE - 1), False)

    def test_is_board_valid_board_in_bound(self):
        self.assertEqual(Field.is_board_valid(Field.MIN_FIELD_SIZE), True)

    def test_get_item_empty(self):
        self.assertEqual(self.field.get_item(1, 1), None)

    def test_get_item_not_empty(self):
        self.field.grid[1][1] = "test"
        self.assertEqual(self.field.get_item(1, 1), "test")

    def test_set_item_works(self):
        self.field.set_item(1, 1, "test")
        self.assertEqual(self.field.grid[1][1], "test")

    def test_set_item_with_no_winner_returns_false(self):
        self.assertEqual(self.field.set_item(1, 1, "test"), False)

    def test_set_item_row_winner_returns_winner(self):
        for item in range(self.field.size - 1):
            self.field.grid[0][item] = "test"
        self.assertEqual(self.field.set_item(0, self.field.size - 1, "test"), "test")

    def test_set_item_col_winner_returns_winner(self):
        for item in range(self.field.size - 1):
            self.field.grid[item][0] = "test"
        self.assertEqual(self.field.set_item(self.field.size - 1, 0, "test"), "test")

    def test_set_item_diagonal_1_winner_returns_winner(self):
        for item in range(self.field.size - 1):
            self.field.grid[item][item] = "test"
        self.assertEqual(self.field.set_item(self.field.size - 1, self.field.size - 1, "test"), "test")

    def test_set_item_diagonal_2_winner_returns_winner(self):
        for item in range(self.field.size - 1):
            self.field.grid[item][self.field.size - item - 1] = "test"
        self.assertEqual(self.field.set_item(self.field.size - 1, 0, "test"), "test")


if __name__ == '__main__':
    unittest.main()

import unittest

from field import Field
from player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("test")
        self.field = Field(3)

    def test_is_player_valid_not_enough_players(self):
        self.assertEqual(Player.is_players_valid(["a" * (Player.ALLOWED_NUMBER_OF_PLAYERS - 1)]), False)

    def test_is_player_valid_too_many_players(self):
        self.assertEqual(Player.is_players_valid(["a" * (Player.ALLOWED_NUMBER_OF_PLAYERS + 1)]), False)

    def test_is_player_valid_enough_players(self):
        self.assertEqual(Player.is_players_valid(["a" * Player.ALLOWED_NUMBER_OF_PLAYERS]), False)

    def test_ai_turn_is_did_not_win(self):
        free_indexes = self.field.get_free_indexes()
        ai_turn_result = self.player.ai_turn(self.field, free_indexes)
        self.assertFalse(ai_turn_result)


if __name__ == '__main__':
    unittest.main()

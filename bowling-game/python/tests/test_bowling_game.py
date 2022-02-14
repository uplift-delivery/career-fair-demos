import unittest
from bowling_game.game import BowlingGame


class TestBowlingGame(unittest.TestCase):
    game: BowlingGame

    def setUp(self) -> None:
        self.game = BowlingGame()

    def test_when_rolling_all_gutter_balls_then_score_is_zero(self):
        self.__rollMany(0, 20)

        self.assertEqual(0, self.game.score())

    def test_when_knocking_down_one_pin_per_roll_then_score_is_twenty(self):
        self.__rollMany(1, 20)

        self.assertEqual(20, self.game.score())

    def test_when_rolling_a_spare_then_score_is_ten_plus_the_next_roll(self):
        self.game.roll(7)
        self.game.roll(3)
        self.game.roll(3)
        self.__rollMany(0, 17)

        self.assertEqual(16, self.game.score())

    def test_when_rolling_a_strike_then_score_is_ten_plus_the_next_two_rolls(self):
        self.game.roll(10)
        self.game.roll(3)
        self.game.roll(3)
        self.__rollMany(0, 16)

        self.assertEqual(22, self.game.score())

    def test_when_rolling_all_strikes_then_score_is_three_hundred(self):
        self.__rollMany(10, 12)

        self.assertEqual(300, self.game.score())

    def __rollMany(self, pins, rolls):
        for index in range(0, rolls):
            self.game.roll(pins)


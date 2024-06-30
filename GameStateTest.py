import unittest

from Card import Card
from GameState import GameState
from Human import Human
from Row import Row


class GameStateTest(unittest.TestCase):
    def setUp(self):
        players = [Human('1'), Human('2')]
        rows = [Row([Card('Fig'), Card('Lime'), Card('Orange')]),
                Row(['Fig']),
                Row(['Lime'])]
        current_player = 0
        self.game_state = GameState(players, rows, current_player)

    def test_take_row(self):
        row = self.game_state.rows[0].cards.copy()
        self.game_state.take_row(0, 0)
        self.assertEqual(self.game_state.players[0].hand.cards, row)
        self.assertEqual(self.game_state.rows[0].cards, [])


if __name__ == '__main__':
    unittest.main()

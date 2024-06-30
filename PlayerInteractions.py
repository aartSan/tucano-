from Hand import Hand
from Player import Player
from Row import Row


class PlayerInteractions:
    # def choose_row(self, hand: Hand, row: Row, player: Player):
    def choose_row(self, player: Player, rows: list[Row], players: list[Player]):  # другие входные параметры
        return player.choose_row(rows, players)

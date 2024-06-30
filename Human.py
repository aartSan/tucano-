from Player import Player
from Row import Row


class Human(Player):
    def choose_row(self, rows: list[Row], players: list[Player]):
        while True:
            row = input(f'{self.name}, выберите колоду (1 =< n =< 3): ')
            try:
                row = int(row)
            except ValueError:
                row = 0
            if 1 <= row <= 3 and rows[row - 1].cards:
                break
        row -= 1
        self.hand.add_cards(rows[row].take_cards())
        return row

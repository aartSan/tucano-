import json
from Player import Player
from Row import Row


class GameState:
    def __init__(self, players: list[Player], rows: list[Row], current_player=0, deck=None):
        self.players = players
        self.current_player = current_player
        self.rows = rows
        self.deck = deck

    # def __repr__(self):
    #     f'players: {self.}'

    def add_cards(self):
        for i in range(len(self.rows)):
            self.rows[i].add_card(self.deck.draw_card())

    def take_row(self, player: int, row: int):
        # self.players[player].choose_row(self.rows[row].take_cards())
        # self.players[player].choose_row(self.rows, self.players)
        self.players[player].hand.add_cards(self.rows[row].take_cards())

    def save(self):
        data = {'players': [player.save() for player in self.players],
                'current_player': self.current_player,
                'rows': [row.save() for row in self.rows],
                'deck': self.deck.save()}
        s = json.dumps(data)
        with open('save-file.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return s

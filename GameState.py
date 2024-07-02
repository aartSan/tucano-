import json

from Deck import Deck
from Player import Player
from Row import Row


class GameState:
    def __init__(self, players: list[Player], rows: list[Row], current_player: int = 0, deck: Deck = None):
        self.players = players
        self.current_player = current_player
        self.rows = rows
        self.deck = deck

    def __str__(self):
        player_names = [p.name for p in self.players]
        return f'Игроки: {player_names}'

    def add_cards(self):
        for i in range(len(self.rows)):
            self.rows[i].add_card(self.deck.draw_card())

    def take_row(self, player: int, row: int):
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

    @classmethod
    def load(cls, file: str):
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        players = [Player.load(p) for p in data['players']]
        current_player = data['current_player']
        rows = [Row.load(row) for row in data['rows']]
        deck = Deck.load(data['deck'])

        return GameState(players, rows, current_player, deck)

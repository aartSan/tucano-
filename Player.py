import json

from Row import Row
from Hand import Hand


# from PlayerInteractions import PlayerInteractions


class Player:
    def __init__(self, name, hand: Hand = None):
        self.name = name
        if hand is None:
            hand = Hand()
        self.hand = hand

    def __repr__(self):
        return f'name: {self.name},\nhand: {self.hand}'

    def __str__(self):
        return f'{self.name}'

    # def choose_row(self, row: Row):
    #     self.hand.add_cards(row.cards)
    def choose_row(self, rows: list[Row], players: list['Player']):
        # self.hand.add_cards(row.cards)
        # return PlayerInteractions.choose_row(self.hand, rows, players)
        raise NotImplementedError("This method should be overridden by subclasses")

    def save(self):
        data = {'name': self.name,
                'hand': self.hand.save()}
        return data

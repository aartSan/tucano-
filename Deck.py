import random
from Card import Card


class Deck:
    def __init__(self, cards=None):
        if cards is None:
            cards = []
            for k, v in Card.CARD_COUNTS.items():
                for i in range(v):
                    cards.append(Card(k))

        self.cards = cards

    def __repr__(self):
        return ' '.join(map(str, self.cards))

    def draw_card(self):
        if self.cards:
            return self.cards.pop()
        return None

    def shuffle(self):
        random.shuffle(self.cards)

    def remaining_cards(self):
        return self.cards.copy()

    def save(self):
        return [c.save() for c in self.cards]


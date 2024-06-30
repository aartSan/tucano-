from Card import Card


class Row:
    def __init__(self, cards: list):
        self.cards = cards
        if cards is None:
            self.cards = []

    def __str__(self):
        return ', '.join(map(str, self.cards))

    def __repr__(self):
        return ' '.join(map(str, self.cards))

    def add_card(self, card: Card):
        if card is None:
            return

        self.cards.append(card)

    def take_cards(self):
        temp = self.cards.copy()
        self.cards.clear()
        return temp

    def save(self):
        return [c.save() for c in self.cards]
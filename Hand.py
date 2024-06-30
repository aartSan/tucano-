from Card import Card


class Hand:
    def __init__(self, cards=None):
        if cards is None:
            cards = []
        self.cards = cards

    def __str__(self):
        return ', '.join(map(str, self.cards))

    def __repr__(self):
        return ' '.join(map(str, self.cards))

    def add_cards(self, cards: list[Card]):
        for c in cards:
            self.cards.append(c)

    def score(self):
        card_counts = self.get_dictionary()
        s = 0
        for k, v in card_counts.items():
            s += Card.score(k, v)
        return s

    def get_dictionary(self):
        card_counts = dict()
        for c in self.cards:
            if c not in card_counts:
                card_counts[c] = 0
            card_counts[c] += 1
        return card_counts

    def save(self):
        return [c.save() for c in self.cards]

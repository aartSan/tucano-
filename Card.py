class Card:
    KINDS = ['Acai', 'Avocado', 'Banana', 'Carambola', 'Coconut',
             'Fig', 'Lime', 'Lychee', 'Orange', 'Papaya',
             'Pineapple', 'Pomegranate', 'Rambutan']

    CARD_COUNTS = {'Acai': 6, 'Avocado': 5, 'Banana': 5, 'Carambola': 5, 'Coconut': 6,
                   'Fig': 4, 'Lime': 2, 'Lychee': 2, 'Orange': 4, 'Papaya': 4,
                   'Pineapple': 3, 'Pomegranate': 6, 'Rambutan': 5}

    CARD_SCORES = {'Acai': (1, 2, 3, 5, 8, 13),
                   'Carambola': (1, 3, 6, 10, 15),
                   'Coconut': (8, 6, 4, 2, 0, -2),
                   'Fig': (-2, 0, 9, 16),
                   'Lime': (-2, -8),
                   'Lychee': (5, 12),
                   'Orange': (4, 8, 12, 0),
                   'Papaya': (1, 1, 9, 20),
                   'Pineapple': (0, -2, -4),
                   'Rambutan': (3, 6, 9, 12, 15)}

    CARD_MULTIPLIERS = {
        'Avocado': (1, 3),  # меньше - больше
        'Banana': (0, 2),  # меньше - больше
        'Pomegranate': (-1, 1),  # меньше - больше
    }

    def __init__(self, kind: str):
        self.kind = kind

    def __repr__(self):
        return self.kind

    def __str__(self):
        return f'{self.kind}'

    def save(self):
        return repr(self)

    @staticmethod
    def score(card: 'Card', count: int):
        card_name = card.kind
        if count == 0:
            return 0
        if card.kind in Card.CARD_MULTIPLIERS:
            return count * Card.CARD_MULTIPLIERS[card_name][0]
        return Card.CARD_SCORES[card_name][count - 1]

class Hand:
    def __init__(self):
        self.cards = []

    def __repr__(self):
        return f"[{', '.join(map(str, self.cards))}]"

    def add_card(self, card):  # добавляет карту на стол
        self.cards.append(card)

    # def remove_card(self, Card):
    #     self.cards.remove(Card)
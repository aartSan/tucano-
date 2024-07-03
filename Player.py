# from AI import AI
# from Human import Human
from Row import Row
from Hand import Hand


class Player:
    def __init__(self, name: str, hand: Hand = None, is_human: bool = False):
        self.name = name
        if hand is None:
            hand = Hand()
        self.hand = hand
        if is_human:
            self.actor = Human()
        else:
            self.actor = AI()

    def __repr__(self):
        return f'name: {self.name},\nhand: {self.hand}'

    def __str__(self):
        return f'{self.name}'

    def choose_row(self, rows: list[Row], players: list['Player']):
        return self.actor.choose_row(self, rows, players)

    def save(self):
        data = {'name': self.name,
                'hand': self.hand.save(),
                'is_human': isinstance(self.actor, Human)}
        return data

    @classmethod
    def load(cls, data: dict):
        name = data['name']
        hand = Hand.load(data['hand'])
        is_human = data['is_human']
        return Player(name, hand, is_human)


class Human:
    @staticmethod
    def choose_row(self, player: Player, rows: list[Row], players: list[Player]):
        while True:
            row = input(f'{player.name}, выберите колоду (1 =< n =< 3): ')
            try:
                row = int(row)
            except ValueError:
                row = 0
            if 1 <= row <= 3 and rows[row - 1].cards:
                break
        row -= 1
        player.hand.add_cards(rows[row].take_cards())
        return row


class AI:
    @staticmethod
    def choose_row(self, player: Player, rows: list[Row], players: list[Player]):
        maxim_score = player.hand.score()
        row = 0
        current_cards = player.hand.cards
        for i in range(len(rows)):
            new_score = Hand(current_cards + rows[i].cards).score()
            if new_score > maxim_score and rows[i].cards:
                row = i
                maxim_score = new_score

        print(f'ИИ "{player.name}" выбирает {row + 1}-ю колоду')
        player.hand.add_cards(rows[row].take_cards())
        return row


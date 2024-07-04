from Card import Card
from Deck import Deck


def test_draw_card():
    deck = Deck([Card('Acai'), Card('Acai'), Card('Acai'), Card('Lychee')])
    card = deck.draw_card()

    assert str(card) == str(Card('Lychee'))
    assert str(deck) == str(Deck([Card('Acai'), Card('Acai'), Card('Acai')]))


def test_remaining_cards():
    deck = Deck([Card('Acai'), Card('Acai'), Card('Acai'), Card('Lychee')])

    assert deck.remaining_cards() == 4



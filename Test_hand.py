from Card import Card
from Hand import Hand


def test_score():
    hand = Hand([Card('Acai'), Card('Acai'), Card('Acai'), Card('Lychee')])
    assert hand.score() == 8


def test_add_cards():
    hand = Hand([Card('Acai'), Card('Acai'), Card('Acai'), Card('Lychee')])
    hand.add_cards([Card('Acai'), Card('Lychee')])
    assert str(hand) == str(Hand([Card('Acai'), Card('Acai'), Card('Acai'), Card('Lychee'),
                          Card('Acai'), Card('Lychee')]))


test_score()
test_add_cards()
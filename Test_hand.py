from Card import Card
from Hand import Hand


def test_score():
    hand1 = Hand([Card('Acai'), Card('Acai'), Card('Acai'), Card('Lychee')])
    hand2 = Hand([Card('Banana'), Card('Banana'), Card('Banana')])
    hand3 = Hand([Card('Banana')])
    hands = [hand1, hand2, hand3]

    assert hand1.score(hands) == 8
    assert hand2.score(hands) == 6
    assert hand3.score(hands) == 0


def test_add_cards():
    hand = Hand([Card('Acai'), Card('Acai'), Card('Acai'), Card('Lychee')])
    hand.add_cards([Card('Acai'), Card('Lychee')])
    assert str(hand) == str(Hand([Card('Acai'), Card('Acai'), Card('Acai'), Card('Lychee'),
                                  Card('Acai'), Card('Lychee')]))


test_score()
test_add_cards()

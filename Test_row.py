import unittest
from Card import Card
from Hand import Hand
from Row import Row


def test_take_cards():
    row = Row([Card('Acai'), Card('Acai'), Card('Acai'), Card('Lychee')])
    hand = Hand()
    hand.add_cards(row.take_cards())
    assert str(hand) == str(Hand([Card('Acai'), Card('Acai'), Card('Acai'), Card('Lychee')]))
    assert row.cards == []


def test_add_card():
    row = Row([Card('Acai'), Card('Acai'), Card('Acai'), Card('Lychee')])
    row.add_card(Card('Acai'))
    assert str(row) == str(Row([Card('Acai'), Card('Acai'), Card('Acai'), Card('Lychee'), Card('Acai')]))


test_take_cards()
test_add_card()
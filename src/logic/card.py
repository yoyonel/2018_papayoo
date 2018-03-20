"""

"""
from enum import Enum
#
from logic.constants import *


class CardSuit(Enum):
    SPADE = 1
    HEART = 2
    DIAMOND = 3
    CLUB = 4
    PAYOO = 5

    @staticmethod
    def to_int(cs):
        return {
            CardSuit.SPADE: 1,
            CardSuit.HEART: 2,
            CardSuit.DIAMOND: 3,
            CardSuit.CLUB: 4,
            CardSuit.PAYOO: 5
        }[cs]

    @staticmethod
    def cards_suits_numbered():
        return [CardSuit.SPADE, CardSuit.HEART, CardSuit.DIAMOND, CardSuit.CLUB]

    @staticmethod
    def to_str(cs):
        """
        https://en.wikipedia.org/wiki/Playing_cards_in_Unicode

        :param cs:
        :return:
        """
        return {
            CardSuit.SPADE: '♠',
            CardSuit.HEART: '♥',
            CardSuit.DIAMOND: '♦',
            CardSuit.CLUB: '♣',
            CardSuit.PAYOO: '🃟'
        }[cs]


class Cards(object):
    def __init__(self, suit, number):
        assert (isinstance(suit, CardSuit))
        assert (
                min(MIN_NUMBER_FOR_PAYOO_CARDS, MIN_NUMBER_FOR_NUMBERED_CARDS)
                <= number <=
                max(MAX_NUMBER_FOR_NUMBERED_CARDS, MAX_NUMBER_FOR_PAYOO_CARDS)
        )
        self._suit = suit
        self._number = number

    def __int__(self):
        return (CardSuit.to_int(self.suit) - 1) * MAX_NUMBER_FOR_NUMBERED_CARDS + self._number

    def __str__(self):
        return "{}{}".format(
            self._number,
            CardSuit.to_str(self._suit),
        )

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        """

        :param other:
        :type other: Cards
        :return:
        """
        return self._suit == other._suit and self._number == other._number

    def __lt__(self, other):
        return int(self) < int(other)

    def from_card(self, other):
        """

        :param other:
        :type other: Cards
        """
        self._number = other.number
        self._suit = other.suit

    @property
    def suit(self):
        return self._suit

    @property
    def number(self):
        return self._number

    def points(self, papayoo_card=None):
        """
        Each Payoo is worth its own rank.
        The Papayoo is worth 40 points and the other cards have no value.

        :return:
        """
        points = POINTS_FOR_NUMBERED_CARDS
        if papayoo_card and self == papayoo_card:
            points = POINTS_FOR_PAPAYOO_CARD
        elif self.suit == CardSuit.PAYOO:
            points = self.number
        return points


class CardsNumbered(Cards):
    def __init__(self, suit, number):
        assert (MIN_NUMBER_FOR_NUMBERED_CARDS <= number <= MAX_NUMBER_FOR_NUMBERED_CARDS)
        super().__init__(suit, number)


class CardsPayoo(Cards):
    def __init__(self, number):
        assert (MIN_NUMBER_FOR_PAYOO_CARDS <= number <= MAX_NUMBER_FOR_PAYOO_CARDS)
        super().__init__(CardSuit.PAYOO, number)


class DiscardCards(object):
    def __init__(self, nb_cards):
        """

        :param nb_cards:
        """
        assert (MIN_DISCARDS_CARDS <= nb_cards <= MAX_DISCARDS_CARDS)
        self._nb_cards = nb_cards

    def __str__(self):
        return "nb_cards={}".format(self._nb_cards)

    @property
    def nb_cards(self):
        return self._nb_cards


class CardPlayed(Cards):
    def __init__(self, player_id, card):
        super().__init__(card.suit, card.number)
        self._player_id = player_id

    @property
    def player_id(self):
        return self._player_id

    def __repr__(self):
        return "(P{}, {})".format(self.player_id, super().__repr__())


def compute_points(cards_played, papayoo_card):
    """

    :param cards_played:
    :type cards_played: list[CardPlayed]
    :param papayoo_card: Papayoo card
    :type papayoo_card: Cards
    :return:
    :rtype: int
    """
    return sum(
        card_played.points(papayoo_card)
        for card_played in cards_played
    )

"""

"""
from enum import Enum


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
        return {
            CardSuit.SPADE: 'spade',
            CardSuit.HEART: 'heart',
            CardSuit.DIAMOND: 'diamond',
            CardSuit.CLUB: 'club',
            CardSuit.PAYOO: 'payoo'
        }[cs]


class Cards(object):
    def __init__(self, suit, number):
        assert (isinstance(suit, CardSuit))
        assert (1 <= number <= 20)
        self._suit = suit
        self._number = number

    def __int__(self):
        return (CardSuit.to_int(self.suit) - 1) * 10 + self._number

    def __str__(self):
        return "(suit={}, number={})".format(
            CardSuit.to_str(self._suit),
            self._number
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
        points = 0
        if papayoo_card and self == papayoo_card:
            points = 40
        elif self.suit == CardSuit.PAYOO:
            points = self.number
        return points


class CardsNumbered(Cards):
    def __init__(self, suit, number):
        assert (1 <= number <= 10)
        super().__init__(suit, number)


class CardsPayoo(Cards):
    def __init__(self, number):
        assert (1 <= number <= 20)
        super().__init__(CardSuit.PAYOO, number)


class DiscardCards(object):
    def __init__(self, nb_cards):
        """

        :param nb_cards:
        """
        assert (3 <= nb_cards <= 5)
        self._nb_cards = nb_cards

    def __str__(self):
        return "nb_cards={}".format(self._nb_cards)

    @property
    def nb_cards(self):
        return self._nb_cards


class CardsToRemoveBeforePlaying(object):
    def __init__(self,
                 cards_to_remove):
        """

        :param cards_to_remove:
        """
        assert (isinstance(cards_to_remove, set))
        self._cards_to_remove = cards_to_remove

    def __str__(self):
        return "cards_to_remove={}".format(self._cards_to_remove)


class CardPlayed(Cards):
    def __init__(self, player_id, card):
        super().__init__(card.suit, card.number)
        self._player_id = player_id

    @property
    def player_id(self):
        return self._player_id

    def __repr__(self):
        return "{} - {}".format(self.player_id, super().__repr__())


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

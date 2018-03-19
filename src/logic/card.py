"""

"""
from collections import defaultdict
from enum import Enum
import random


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


class NumberOfCardsPerPlayer(object):
    def __init__(self,
                 number_of_players,
                 three_times,
                 one_card):
        assert (3 <= number_of_players <= 8)
        assert (2 <= three_times <= 6)
        assert (0 <= one_card <= 2)
        if number_of_players < 7:
            self._total_cards = 60
        else:
            self._total_cards = 60 - 4
        assert ((three_times * 3 + one_card) * number_of_players == self._total_cards)
        self._three_times = three_times
        self._one_card = one_card

    @property
    def total_cards(self):
        return self._total_cards

    @property
    def three_times(self):
        return self._three_times

    @property
    def one_card(self):
        return self._one_card

    def __str__(self):
        return "tree_times={}, one_card={}".format(
            self._three_times,
            self._one_card
        )


def builder_number_of_cards_per_player(nb_players):
    """

    :param nb_players:
    :type nb_players: int
    :return:
    :rtype: NumberOfCardsPerPlayer
    """
    return {
        3: NumberOfCardsPerPlayer(3, 6, 2),
        4: NumberOfCardsPerPlayer(4, 5, 0),
        5: NumberOfCardsPerPlayer(5, 4, 0),
        6: NumberOfCardsPerPlayer(6, 3, 1),
        7: NumberOfCardsPerPlayer(7, 2, 2),
        8: NumberOfCardsPerPlayer(8, 2, 1),
    }[nb_players]


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


def builder_discard_cards(nb_players):
    """

    :param nb_players:
    :type nb_players: int
    :return:
    :rtype: DiscardCards
    """
    return {
        3: DiscardCards(5),
        4: DiscardCards(5),
        5: DiscardCards(4),
        6: DiscardCards(3),
        7: DiscardCards(3),
        8: DiscardCards(3)
    }[nb_players]


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


def builder_cards_to_remove_before_players(nb_players):
    """

    :param nb_players:
    :type nb_players: int
    :return:
    """
    if nb_players < 7:  # 3 to 6 players
        return []
    else:  # for 7 & 8 players
        return [
            CardsNumbered(CardSuit.CLUB, 1),
            CardsNumbered(CardSuit.DIAMOND, 1),
            CardsNumbered(CardSuit.HEART, 1),
            CardsNumbered(CardSuit.SPADE, 1),
        ]


class DealingCards(object):
    def __init__(self, nb_players):
        """

        :param nb_players:
        """
        assert (3 <= nb_players <= 8)
        #
        self._nb_players = nb_players
        #
        self._cards_to_remove_before_playing = builder_cards_to_remove_before_players(nb_players)
        self._number_of_cards_per_player = builder_number_of_cards_per_player(nb_players)
        self._discard = builder_discard_cards(nb_players)
        #
        self._cards = []
        self.reset()

    @property
    def discard(self):
        return self._discard

    def reset(self):
        self._cards = [
            CardsNumbered(suit, number)
            for suit in CardSuit
            for number in range(1, 11)
        ]
        self._cards += [CardsPayoo(number) for number in range(11, 21)]
        #
        self._cards = [
            card
            for card in self._cards
            if card not in self._cards_to_remove_before_playing
        ]
        assert len(self._cards) == self._number_of_cards_per_player.total_cards

    def __str__(self):
        return "nb player={NB_PLAYERS}, " \
               "cards to remove before player={CARDS_TO_REMOVE_BEFORE_PLAYING}, " \
               "number of cards per player={NUMBER_OF_CARDS_PER_PLAYER}, " \
               "discard cards={DISCARD_CARDS}".format(
                    NB_PLAYERS=self._nb_players,
                    CARDS_TO_REMOVE_BEFORE_PLAYING=self._cards_to_remove_before_playing,
                    NUMBER_OF_CARDS_PER_PLAYER=self._number_of_cards_per_player,
                    DISCARD_CARDS=self._discard
                )

    def dealing(self, shuffle_cards=True):
        """

        :param shuffle_cards: shuffle cards (in place)
        :type shuffle_cards: bool
        :return: return cards distribution (for each player)
        :rtype: dict
        """
        deal = defaultdict(list)
        #
        if shuffle_cards:
            random.shuffle(self._cards)
        #
        cur_id_card = 0
        three_times_nb_cards = self._number_of_cards_per_player.three_times
        nb_times_one_card = self._number_of_cards_per_player.one_card
        for _ in range(3):
            for id_player in range(self._nb_players):
                deal[id_player].extend(self._cards[cur_id_card:cur_id_card + three_times_nb_cards])
                cur_id_card += three_times_nb_cards
        for _ in range(nb_times_one_card):
            for id_player in range(self._nb_players):
                deal[id_player].extend(self._cards[cur_id_card:cur_id_card + 1])
                cur_id_card += 1
        assert cur_id_card == self._number_of_cards_per_player.total_cards
        return dict(deal)


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

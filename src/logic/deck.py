"""

"""
from collections import defaultdict
import random

from logic.card import CardsNumbered
from logic.card import CardsPayoo
from logic.card import CardSuit
from logic.card import DiscardCards

from logic.constants import *


class DealingCards(object):
    """

    """
    def __init__(self, nb_players):
        """

        :param nb_players:
        """
        assert (MIN_PLAYERS <= nb_players <= MAX_PLAYERS)
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
            for number in range(MIN_NUMBER_FOR_PAYOO_CARDS, MAX_NUMBER_FOR_NUMBERED_CARDS+1)
        ]
        self._cards += [
            CardsPayoo(number)
            for number in range(MAX_NUMBER_FOR_NUMBERED_CARDS+1, MAX_NUMBER_FOR_PAYOO_CARDS+1)
        ]
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
        nb_times_three_cards = NB_TIMES_THREE_CARDS
        for _ in range(nb_times_three_cards):
            for id_player in range(self._nb_players):
                deal[id_player].extend(self._cards[cur_id_card:cur_id_card + three_times_nb_cards])
                cur_id_card += three_times_nb_cards
        for _ in range(nb_times_one_card):
            for id_player in range(self._nb_players):
                deal[id_player].extend(self._cards[cur_id_card:cur_id_card + 1])
                cur_id_card += 1
        assert cur_id_card == self._number_of_cards_per_player.total_cards
        return dict(deal)


class NumberOfCardsPerPlayer(object):
    """

    """
    def __init__(self,
                 number_of_players,
                 three_times,
                 one_card):
        assert (MIN_PLAYERS <= number_of_players <= MAX_PLAYERS)
        assert (MIN_CARDS_FOR_DEALING_THREE_TIMES <= three_times <= MAX_CARDS_FOR_DEALING_THREE_TIMES)
        assert (MIN_LOOPS_FOR_DEALING_ONE_CARD <= one_card <= MAX_LOOPS_FOR_DEALING_ONE_CARD)
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

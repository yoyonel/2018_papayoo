"""

"""


class Player(object):
    def __init__(self,
                 player_id,
                 player_name=None):
        """

        :param player_id:
        :param player_name:
        """
        assert (0 <= player_id <= 7)
        self._player_id = player_id
        if player_name:
            self._player_name = player_name
        else:
            self._player_name = "Player {}".format(player_id)
        #
        self._game_points = 0
        self._round_points = 0
        self._round_id = 0
        #
        self._cards = []
        self._discard_cards = []
        #
        self._papayoo = None

    @property
    def cards(self):
        return self._cards

    @property
    def name(self):
        return self._player_name

    @property
    def round_points(self):
        return self._round_points

    @property
    def papayoo(self):
        return self._papayoo

    @papayoo.setter
    def papayoo(self, c):
        """

        :param c:
        :type c: Cards
        """
        self._papayoo = c

    def add_cards(self, cards):
        """

        :param cards:
        :type cards: list(Cards)
        :return:
        """
        self._cards.extend(cards)

    def remove_cards(self, removed_cards):
        """

        :param removed_cards:
        :return:
        """
        self._cards = [
            card
            for card in self._cards
            if card not in removed_cards
        ]

    def __repr__(self):
        return "{}/{}\n{}".format(
            self._player_id, self._player_name,
            self._cards
        )

    def add_points(self, points):
        """

        :param points:
        :return:
        """
        self._game_points += points
        self._round_points += points

    def add_discard_cards(self, discard_cards):
        """

        :param discard_cards:
        :return:
        """
        self._discard_cards.extend(discard_cards)

    def finish_discard_step(self):
        self._cards.extend(self._discard_cards)

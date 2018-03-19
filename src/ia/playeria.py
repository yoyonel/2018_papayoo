"""

"""
from src.logic.player import Player


class PlayerIA(Player):
    """
    Interface (~ virtual class) of IA for Player

    """
    def __init__(self,
                 player_id,
                 player_name=None):
        """

        :param player_id:
        :param player_name:
        """
        super().__init__(player_id, player_name)

    def do_discards(self, discard):
        """

        :param discard:
        :type discard: DiscardCards
        :return:
        :rtype: list[Cards]
        """
        raise NotImplemented("Not implemented!")

    def get_from_discards(self, cards):
        """

        :param cards:
        :type cards: list[Cards]
        :return:
        """
        raise NotImplemented("Not implemented!")

    def play(self, cards_already_played):
        """

        :param cards_already_played:
        :type cards_already_played: list[Cards]
        :return:
        """
        raise NotImplemented("Not implemented!")

"""

"""
import random
#
from src.ia.playeria import PlayerIA


class RandomPlayerIA(PlayerIA):
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
        def _choose_discard_cards():
            id_cards = list(range(len(self._cards)))
            random.shuffle(id_cards)
            return [
                self._cards[id_card]
                for id_card in id_cards[:discard.nb_cards]
            ]
        #
        discard_cards = _choose_discard_cards()
        #
        self.remove_cards(discard_cards)
        #
        return discard_cards

    def get_from_discards(self, cards):
        """

        :param cards:
        :type cards: list[Cards]
        :return:
        """
        # self.add_cards(cards)
        self.add_discard_cards(cards)

    def play(self, cards_already_played):
        """

        :param cards_already_played:
        :type cards_already_played: list[tuple(int, Cards)]
        :return:
        :rtype: Cards
        """
        cards_playable = self._cards
        # filter cards we can play
        if cards_already_played:
            first_card_play = cards_already_played[0]
            filter_suit = first_card_play.suit
            filter_cards_playable = [
                card
                for card in self._cards
                if card.suit == filter_suit
            ]
            if filter_cards_playable:
                cards_playable = filter_cards_playable
        #
        play_card = random.choice(cards_playable)
        self.remove_cards([play_card])
        return play_card

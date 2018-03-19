"""

"""
from src.ia.playeria import PlayerIA


class MinMaxPlayerIA(PlayerIA):
    """

    """
    def __init__(self,
                 player_id,
                 player_name=None):
        """

        :param player_id:
        :param player_name:
        """
        super().__init__(player_id, player_name)

    def _sort_by_points_and_numbers(self, cards=None):
        """

        :param cards:
        :type cards: list[Cards] | None
        :return:
        """
        return sorted(
            cards if cards is not None else self.cards,
            key=lambda c: c.points(self.papayoo)*100 + c.number,
            reverse=True,
        )

    def do_discards(self, discard):
        """

        :param discard:
        :type discard: DiscardCards
        :return:
        :rtype: list[Cards]
        """
        def _choose_discard_cards():
            cards_sorted = self._sort_by_points_and_numbers()
            return cards_sorted[:discard.nb_cards]
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
        self.add_discard_cards(cards)

    def play(self, cards_already_played):
        """

        :param cards_already_played:
        :type cards_already_played: list[tuple(int, Cards)]
        :return:
        :rtype: Cards
        """
        cards_sorted = self._sort_by_points_and_numbers()

        if len(cards_already_played) == 0:
            # get min card
            play_card = cards_sorted[-1]    # min
        else:
            # filter cards we can play
            first_card_play = cards_already_played[0]
            filter_suit = first_card_play.suit
            filter_cards_playable = [
                card
                for card in cards_sorted
                if card.suit == filter_suit
            ]
            if len(filter_cards_playable) == 0:
                # defausse
                play_card = cards_sorted[0]    # max
            else:
                # peut on "sous jouer" (ne pas prendre la main) ?
                filter_cards_without_taking_hand = [
                    card
                    for card in filter_cards_playable
                    if card.number < first_card_play.number
                ]
                if len(filter_cards_without_taking_hand) == 0:
                    # on a que des cartes pour prendre la main
                    # on prend la plus grande
                    play_card = filter_cards_playable[0]    # max
                    # exception pour le papayoo :p
                    if play_card == self.papayoo:
                        try:
                            play_card = filter_cards_playable[1]
                        except IndexError:
                            # en fait on n'a pas le choix :'(
                            pass
                else:
                    # on a des cartes à jouer sans prendre la main
                    # on choisit la carte la plus élevée (en points ou nombres)
                    play_card = filter_cards_without_taking_hand[0]     # max
        # remove this card (from hand)
        self.remove_cards([play_card])
        # return the played card
        return play_card

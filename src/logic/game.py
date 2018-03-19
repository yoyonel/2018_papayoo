"""

"""
import logging
import random
#
from ia.random_playeria import RandomPlayerIA
from ia.minmax_playeria import MinMaxPlayerIA
from logic.card import Cards
from logic.card import CardSuit
from logic.card import CardPlayed
from logic.card import compute_points
from logic.deck import DealingCards


logger = logging.getLogger(__name__)


def play(nb_players):
    """

    :param nb_players:
    :type nb_players: int
    """
    dealing_cards = DealingCards(nb_players=nb_players)
    players = {}  # dict[int, Players]
    ia_players = [
        RandomPlayerIA,
        MinMaxPlayerIA,
    ]
    for player_id, player_cards in dealing_cards.dealing().items():
        players[player_id] = ia_players[player_id % len(ia_players)](player_id)
        logger.debug("Player id={} -> {}".format(player_id, type(players[player_id])))
        player = players[player_id]
        player.add_cards(player_cards)

    # choosing papayoo suit
    suit_for_papayoo = random.choice(CardSuit.cards_suits_numbered())
    papayoo_card = Cards(suit_for_papayoo, 7)
    logger.info("* Choosing papayoo: {}".format(papayoo_card))

    # step: Discards
    logger.info("* Discard step")
    for player_id in range(nb_players):
        next_player_id = (player_id + 1) % nb_players
        cur_player = players[player_id]
        next_player = players[next_player_id]
        # choose discards cards
        discard_cards = cur_player.do_discards(dealing_cards.discard)
        next_player.get_from_discards(discard_cards)
        # set papayoo card
        cur_player.papayoo = papayoo_card
        #
        logger.debug("current player id={}".format(player_id))
        logger.debug("next player id={}".format(next_player_id))
        logger.debug("discard_cards={}".format(discard_cards))
    for player in players.values():
        player.finish_discard_step()

    logger.info("* Main Loop")
    nb_games_in_round = 0
    nb_rounds = 0
    try:
        id_player_win = 0
        while True:
            cards_played = []
            for player_id in range(nb_players):
                player_id = (player_id + id_player_win) % nb_players
                card_played = players[player_id].play(cards_played)
                logger.info(
                    "{} - {}{}".format(
                        players[player_id].name,
                        '🃏' if card_played == papayoo_card else '',
                        card_played,
                    )
                )
                cards_played.append(CardPlayed(player_id, card_played))
            #
            first_card_played = cards_played[0]
            cards_played_sorted = sorted(
                cards_played,
                key=lambda cp: cp.number if cp.suit == first_card_played.suit else 0,
                reverse=True,
            )
            logger.debug("cards_played_sorted: {}".format(cards_played_sorted))
            id_player_win = cards_played_sorted[0].player_id
            logger.info("-> id player win/loose: {}".format(players[id_player_win].name))
            # compute points
            points = compute_points(cards_played, papayoo_card)
            logger.info("-> take {} points".format(points))
            # attribute points to "winner"
            players[id_player_win].add_points(points)
            # next round
            nb_games_in_round += 1
    except IndexError:
        logger.debug("End of round={}".format(nb_rounds))
        logger.debug("Nb games in round={}".format(nb_games_in_round))
    except Exception as e:
        logger.error("Error during main loop!")
        raise e

    total_points = 0
    for player_id, player in players.items():
        logger.info("{} take {} points on this round".format(players[player_id].name, player.round_points))
        total_points += player.round_points
    logger.debug("Total points for this round={}".format(total_points))

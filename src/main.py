"""

"""
import logging
import os
#
import src.logic.game as game

logger = logging.getLogger(__name__)


def main():
    nb_players = 6
    game.play(nb_players)


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=os.environ.get("LOGLEVEL", "DEBUG"),
    )
    main()

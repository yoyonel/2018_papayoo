"""

"""
import logging
import os
#
import logic.game as game

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=os.environ.get("LOGLEVEL", "DEBUG"),
    )
    nb_players = 6
    game.play(nb_players)


if __name__ == '__main__':
    main()

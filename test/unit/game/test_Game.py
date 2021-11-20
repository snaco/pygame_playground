from src.game import Game
from src.entities import GameConfig
from pytest import raises
import pygame

def test_start_loop_without_priming_engine(mocker, game_config):
    mocker.patch('pygame.init')
    mocker.patch('src.game.Game._load_config', return_value=GameConfig(game_config))
    game = Game()
    with raises(Exception):
        game.start_loop()

def test_start_loop(mocker, game_config):
    mocker.patch('pygame.init')
    mocker.patch('pygame.event.poll', return_value=pygame.QUIT)
    mocker.patch('src.game.Game._load_config', return_value=GameConfig(game_config))
    game = Game()
    game.prime_engine()
    assert game.start_loop()
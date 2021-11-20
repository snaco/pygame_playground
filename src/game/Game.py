import json
from typing import List, Callable

import pygame

from src.entities import GameConfig


class Game():
    """
    This object controls the core functionality of the game
    Game().context offers a dict to attach ad-hoc variables to for whatever you want
    """
    def __init__(self):
        self.config = self._load_config()
        self.running = False
        pre_launch_tasks: List[Callable] = []
        starting_tasks: List[Callable] = [self._initialize_game_window]
        closing_tasks: List[Callable] = []
        loop_tasks: List[Callable] = []
        self.tasks = {
            'launch': pre_launch_tasks,
            'start': starting_tasks,
            'loop': loop_tasks,
            'close': closing_tasks
        }
        self.context = {}

    def _initialize_game_window(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.config.window_size)
        self.clock = pygame.time.Clock()

    def _do_pre_launch_tasks(self):
        print('Running pre-launch tasks...')
        for task in self.tasks['launch']:
            task()

    def _do_starting_tasks(self):
        print('Running startup tasks...')
        for task in self.tasks['start']:
            task()
        print('Done!')

    def _do_closing_tasks(self):
        print('Running closing tasks...')
        for task in self.tasks['close']:
            task()
        print('Done!')

    def _load_config(self):
        with open('game_config.json', 'r') as config_file:
            config_file = json.loads(config_file.read())
            return GameConfig(config_file)

    def add_task(self, task_group: str, task: Callable):
        self.tasks[task_group].append(task)

    def prime_engine(self):
        """Literally pointless but it's fun"""
        self.running = True

    def activate_kill_switch(self):
        """Literally pointless but it's fun"""
        self.running = False

    def start_loop(self) -> bool:
        """run the main game loop"""
        if not self.running:
            raise Exception('You forgot to prime the engine!')
        self._do_pre_launch_tasks()
        self._do_starting_tasks()
        while self.running:
            event = pygame.event.poll()
            if event == pygame.QUIT:
                self.running = False
            if event == pygame.K_ESCAPE:
                self.running = False
            for task in self.tasks['loop']:
                task()
            pygame.display.update()
            self.clock.tick(self.config.frame_rate)
        self._do_closing_tasks()
        pygame.quit()
        return True
"""
Entity objects live here
"""
from dataclasses import dataclass

class GameConfig():
    """Object for storing game config info"""

    def __init__(self, config_file: dict):
        self.height = config_file['height']
        self.width = config_file['width']
        self.window_size = (self.width, self.height)

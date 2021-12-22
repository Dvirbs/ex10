from typing import *
import game_parameters

class Apple:
    """
    Apple type object
    """
    INITIAL_SCORE = 0
    COLOR = "green"
    def __init__(self):
        """
        initialize Apple object:
        location: none, color: COLOR, score: initial score
        """
        self.__locatation = None
        self.__score = self.INITIAL_SCORE
        self.__color = self.COLOR

    def set_color(self, color: str) -> None:
        self.__color = color

    def get_color(self) -> str:
        return self.__color

    def set_apple(self) -> None:
        """set random data to the apple"""
        x, y, score = game_parameters.get_random_apple_data()
        self.__locatation = x, y
        self.__score = score

    def get_location(self) -> Tuple:
        return self.__locatation

    def get_score(self) -> int:
        return self.__score
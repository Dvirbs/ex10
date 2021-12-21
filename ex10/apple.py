from typing import *
import game_parameters

class Apple:
    """
    Apple object
    """

    def __init__(self):
        """
        A constructor for a Apple object
        :param location: A tuple representing the aplle (row, col) location
        """
        # check conditions if the inputs is correct
        self.__locatation = None
        self.__score = 0
        self.__color = None


    def set_color(self, color: str) -> None:
        self.__color = color

    def get_color(self) -> str:
        return self.__color

    def set_apple(self) -> None:
        x, y, score = game_parameters.get_random_apple_data()
        self.__locatation = x, y
        self.__score = score

    def get_location(self) -> Tuple:
        return self.__locatation

    def get_score(self) -> int:
        return self.__score



import game_parameters
from typing import *

class Bomb:
    """
    Bomb object
    """
    COLOR = "red"
    ZERO_REDIUS = 0
    TIME_CONST = 1

    def __init__(self):
        """
        init the bomb with location raius and time
        """
        self.__location: Tuple = None
        self.__radius: int = None
        self.__time : int = None

    def get_location(self) -> Tuple:
        return self.__location

    def set_bomb(self) -> None:
        """
        set bomb with location, radius and time
        """
        x, y, radius, time = game_parameters.get_random_bomb_data()  # הכנסת המידע לתוך רשימה
        self.__location = x, y
        self.__radius = radius
        self.__time = time

    def blast_cords(self):
        """
        function that returning a list of the current blast wave for the specif time
        :return:  List of blast cells
        """
        # i tried to put the mext paramter but it couse some problem
        # self.__location[0] = x
        # self.__location[1] = y
        radius = self.get_time()
        if radius == 0:
            return [(self.__location[0], self.__location[1])]
        if radius < 0:
            radius = -1 * radius
        blast_cords_list: List[Tuple] = [(self.__location[0], self.__location[1] + radius),
                                         (self.__location[0], self.__location[1] - radius),
                                         (self.__location[0] + radius, self.__location[1]),
                                         (self.__location[0] - radius, self.__location[1])]
        row_jump = 1
        for col_i in range(self.__location[0] - radius + 1, self.__location[0], 1):
            blast_cords_list.append((col_i, self.__location[1] + row_jump))
            blast_cords_list.append((col_i, self.__location[1] - row_jump))
            row_jump += 1
        row_jump = 1
        for col_i in range(self.__location[0] + radius - 1, self.__location[0], -1):
            blast_cords_list.append((col_i, self.__location[1] + row_jump))
            blast_cords_list.append((col_i, self.__location[1] - row_jump))
            row_jump += 1
        return blast_cords_list

    def time_getting_smaller(self) -> None:
        self.__time -= self.TIME_CONST

    def get_time(self) -> int:
        return self.__time

    def get_redius(self) -> int:
        return self.__radius

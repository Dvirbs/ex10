from node import Node
from typing import *

class Snake:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__length = 0
        self.__color = None
        self.__move_direcation = 'Right'
        self.__locations = []

    def add_new_head(self, new_head: Tuple[int, int]) -> None:
        """
        adds a location to the snake's head
        :param new_head: tuple of new head location
        :return: None
        """
        self.__length += 1
        self.__locations.append(new_head) #TODO add to the begining

    def get_location(self):
        return self.__locations

    def get_head(self) -> Tuple[int, int]:
        return self.__locations[0]

    def get_tail(self) -> Tuple[int, int]:
        return self.__locations[-1]

    def remove_tail(self):
        """
        rmove the location of the snake's tail
        :return: None
        """
        self.__length -= 1
        self.__locations = self.get_location()[:-1]

    def set_color(self, color: str):
        self.__color = color

    def possible_moves(self):
        """מחזירה על סמך הכיוון הנוכחי של הנחש מהם המהלכים האפשריים"""
        if self.__orientation == "Right":
            return ["Down", "Up"]
        if self.__orientation == "Left":
            return ["Down", "Up"]
        if self.__orientation == "Up":
            return ["Right", "Left"]
        if self.__orientation == "Down":
            return ["Right", "Left"]

    def set_orientation(self, movekey):
        possible_move = self.possible_moves()
        if movekey in possible_move:  # אם הכיוון נמצא ברשימת הכיוונים - נעדכן את הכיוון.
            self.__orientation = movekey

    def move(self):
        """פונקציה המקבלת כיוון ומחזירה אמת אם הנחש זז בהצלחה, שקר אחרת"""
        row_head = self.get_head()[0]
        col_head = self.get_head()[1]

        if self.__orientation == "Right":
            x = row_head
            y = col_head + 1
        elif self.__orientation == "Left":
            x = row_head
            y = col_head - 1
        elif self.__orientation == "Down":
            x = row_head + 1
            y = col_head
        else:
            x = row_head - 1
            y = col_head
        # if self.in_crash((x, y)):  # אם הראש העתידי של הנחש יפגע בגופו נחזיר False
        #      return False
        new_head = (x, y)
        self.add_new_head(new_head)
        self.remove_tail()
        return True


s = Snake()
head = (7, 10)
s.add_new_head(head)
head = (7, 11)
s.add_new_head(head)
head = (7, 12)
s.add_new_head(head)
print(s.get_location())
s.move()
print(s.get_location())

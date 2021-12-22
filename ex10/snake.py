from typing import *
class Snake:
    """
    Snake object:
    The snake is defined by a list where the first element in the
    list represents the head while the last one represents the tail.
    The snake has a direction of movement and color.
    """
    COLOR = "black"
    INITIAL_ORIENTATION = "Up"
    INITIAL_LENGTH = 0
    def __init__(self):
        """
        initialize Apple object:
        head: none, tail: none, length: initial length, color: initial color,
        orientation: initial orientation, locations: empty list.
        """
        self.__head = None
        self.__tail = None
        self.__length = self.INITIAL_LENGTH
        self.__color = self.COLOR
        self.__orientation = self.INITIAL_ORIENTATION
        self.__locations = []

    def get_length(self):
        return self.__length

    def add_new_head(self, new_head: Tuple[int, int]) -> None:
        """
        add new head to the snake.
        :param new_head: tuple of new head location
        :return: None
        """
        self.__length += 1
        self.__locations.insert(0,new_head) #TODO add to the begining

    def get_locations(self) -> List:
        return self.__locations

    def get_head(self) -> Tuple[int, int]:
        return self.__locations[0]

    def get_tail(self) -> Tuple[int, int]:
        return self.__locations[-1]

    def add_to_tail(self, new_tail: Tuple[int, int]) -> None:
        self.__length += 1
        self.__locations.append(new_tail)

    def remove_tail(self):
        """
        remove the cell of the snake's tail
        :return: None
        """
        self.__length -= 1
        return self.get_locations().pop()

    def remove_head(self):
        """
        remove the cell of the snake's head
        :return: None
        """
        self.__length -= 1
        return self.get_locations().pop(0)

    def set_color(self, color: str):
        self.__color = color

    def possible_moves(self):
        """Returns based on the current direction of the snake the possible moves"""
        if self.__orientation == "Right":
            return ["Down", "Up"]
        if self.__orientation == "Left":
            return ["Down", "Up"]
        if self.__orientation == "Up":
            return ["Right", "Left"]
        if self.__orientation == "Down":
            return ["Right", "Left"]

    def set_orientation(self, movekey):
        """Updates the direction of the snake"""
        possible_move = self.possible_moves()
        # If a direction is in the direction list we will update it
        if movekey in possible_move:
            self.__orientation = movekey

    def move(self):
        """A function that advances the snake one step in the current direction.
            Return the deleted tail.
        """
        column_head = self.get_head()[0]
        row_head = self.get_head()[1]

        if self.__orientation == "Up":
            x = column_head
            y = row_head + 1
        elif self.__orientation == "Down":
            x = column_head
            y = row_head - 1
        elif self.__orientation == "Right":
            x = column_head + 1
            y = row_head
        else:
            x = column_head - 1
            y = row_head
        new_head = (x, y)
        self.add_new_head(new_head)
        return self.remove_tail()
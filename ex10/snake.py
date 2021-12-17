from node import Node

class Snake:
    def __init__(self):
        self.__head: Node = None
        self.__tail: Node = None
        self.__length = 0
        self.__color = None
        self.__move_direcation = None

    def set_new_head(self, new_head: Node) -> None:
        self.__length += 1
        if self.__head is None:
            self.__head = new_head
        else:
            self.__head = self.__head.get_next()
            self.__head.get_prev().set_next(new_head)

    def get_head(self) -> Node:
        return self.__head

    def remove_tail(self):
        if self.__tail is None:
            print('there is someting wrong, the snake is None')
        else:
            self.__tail = self.__tail.get_next()
            self.__tail.get_prev().set_next(None)
            self.__tail.set_prev(None)

    def set_color(self, color: str):
        self.__color = color

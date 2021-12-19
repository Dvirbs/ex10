from node import Node

class Snake:
    def __init__(self):
        self.__head: Node = None
        self.__tail: Node = None
        self.__length = 0
        self.__color = None
        self.__move_direcation = None

    def add_new_head(self, new_head: Node) -> None:
        self.__length += 1
        if self.__head is None:
            self.__head = new_head
        else:
            new_head.set_prev(self.__head)
            self.__head.set_next(new_head)
            self.__head = self.__head.get_next()

    # def add_tail(self, new_head: Node) -> None:
    #     self.__length += 1
    #     self.__tail = 5

    def get_head(self) -> Node:
        return self.__head

    def remove_tail(self):
        self.__length -= 1

        if self.__tail is None:
            print('there is someting wrong, the snake is None')
        else:
            self.__tail = self.__tail.get_next()
            self.__tail.get_prev().set_next(None)
            self.__tail.set_prev(None)

    def set_color(self, color: str):
        self.__color = color


s = Snake()
s.orientation = "Up"
head = Node((7,10))
s.add_new_head(head)
print(s.get_head().get_data())
head2 = Node((8,10))
s.add_new_head(head2)
print(s.get_head().get_data())

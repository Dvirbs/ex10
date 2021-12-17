class Node:
    def __init__(self, prev=None, next=None):
        self.data = 'Black'  # TODO how to fulfill the data for black pixel
        self.prev = prev
        self.next = next

#ddלשג
class SnakeDoubleLinkedList:
    """
    create a snake
    """

    def __init__(self):
        self.__head = self.__tail = None
        self.__length = 0

    def add_first(self, node):
        if self.__head is None:
            # list was empty
            self.__head = self.__tail = node
        else:
            # connect old head to new node
            self.__head.prev = node
            self.next = self.__head

        # update head
        self.__head = node
        self.__length += 1

    def remove_last(self):
        if self.__head is None:
            # list was empty
            print('canot move last because the List is empty')
        else:
            self.__tail = self.__tail.prev
            if self.__tail is None: # list is now empty
                self.__head = None
            else: # disconnect old tail
                self.__tail.next.prev = None
                self.__tail.next = None
            self.__length -=1




snake = SnakeDoubleLinkedList
snake_head = Node('head')
print(snake, type(snake))
print(snake_head, type(snake_head))

snake.add_first(snake_head)



from typing import *


class Node:
    def __init__(self, data: Tuple[int, int], prev: Node = None, next: Node = None):
        self.__data = data
        self.__prev = prev
        self.__next = prev

    def set_data(self, data: Tuple[int, int]) -> None:
        self.__data = data

    def get_data(self) -> Tuple[int, int]:
        return self.__data

    def set_prev(self, prev: Node) -> None:
        self.__prev = prev

    def get_prev(self) -> Node:
        return self.__prev

    def set_next(self, next: Node) -> None:
        self.__next = next

    def get_next(self) -> Node:
        return self.__next


from typing import *


class Node:
    def __init__(self, data: Tuple[int, int], prev = None, next = None):
        self.__data = data
        self.__prev = prev
        self.__next = prev

    def set_data(self, data: Tuple[int, int]) -> None:
        self.__data = data

    def get_data(self) -> Tuple[int, int]:
        return self.__data

    def set_prev(self, prev) -> None:
        self.__prev = prev

    def get_prev(self):
        return self.__prev

    def set_next(self, next) -> None:
        self.__next = next

    def get_next(self):
        return self.__next


import game_parameters


class Bomb:
    COLOR = "red"

    def __init__(self):
        self.__location = None
        self.__radius = None
        self.__time = None

    def get_location(self):
        return self.__location

    def set_bomb(self):
        x, y, radius, time = game_parameters.get_random_bomb_data()  # הכנסת המידע לתוך רשימה
        self.__location = x, y
        self.__radius = radius
        self.__time = 3  #time

    def blast_cords(self):
        radius = self.get_time()
        if radius < 0:
            radius = -1 * radius
        blast_cords_list: List[Tuple] = [(self.__location[0], self.__location[1] + radius),
                                         (self.__location[0], self.__location[1] - radius),
                                         (self.__location[0] + radius, self.__location[1]),
                                         (self.__location[0] - radius, self.__location[1])]
        j = 1
        for i in range(self.__location[0] - radius + 1, self.__location[0], 1):
            blast_cords_list.append((i, self.__location[1] + j))
            blast_cords_list.append((i, self.__location[1] - j))
            j += 1
        j = 1
        for i in range(self.__location[0] + radius - 1, self.__location[0], -1):
            blast_cords_list.append((i, self.__location[1] + j))
            blast_cords_list.append((i, self.__location[1] - j))
            j += 1
        return blast_cords_list

    def time_getting_smaller(self) -> None:
        self.__time -= 1

    def get_time(self) -> int:
        return self.__time

    def get_redius(self) -> int:
        return self.__radius

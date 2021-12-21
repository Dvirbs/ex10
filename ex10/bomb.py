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
        column, row, radius, time = game_parameters.get_random_bomb_data()  # הכנסת המידע לתוך רשימה
        self.__location = column, row
        self.__radius = radius
        self.__time = time

    def coordinates_by_radius(self, radius):
        if radius == 0:
            return self.__location
        if radius < 0:
            radius = -1*radius
        v = [(self.__location[0], self.__location[1] + radius), (self.__location[0], self.__location[1] - radius),
             (self.__location[0] + radius, self.__location[1]), (self.__location[0] - radius, self.__location[1])]
        j = 1
        for i in range(self.__location[0] - radius + 1, self.__location[0], 1):
            v.append((i, self.__location[1] + j))
            v.append((i, self.__location[1] - j))
            j += 1
        j = 1
        for i in range(self.__location[0] + radius - 1, self.__location[0], -1):
            v.append((i, self.__location[1] + j))
            v.append((i, self.__location[1] - j))
            j += 1
        return v

    def update_time(self, time):
        """
        :param crds_loc: A tuple representing the coords of the required location.
        :return: True upon success, False otherwise
        """
        self.__time = time







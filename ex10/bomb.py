import game_parameters
class Bomb:
    COLOR = "red"

    def __init__(self, location, radius, time):
        self.location = location
        self.radius = radius
        self.time = time

    def coordinates_by_radius(self, radius):
        if radius == 0:
            return self.location
        if radius < 0:
            radius = -1*radius
        v = [(self.location[0], self.location[1] + radius), (self.location[0], self.location[1] - radius),
             (self.location[0] + radius, self.location[1]), (self.location[0] - radius, self.location[1])]
        j = 1
        for i in range(self.location[0] - radius + 1, self.location[0], 1):
            v.append((i, self.location[1] + j))
            v.append((i, self.location[1] - j))
            j += 1
        j = 1
        for i in range(self.location[0] + radius - 1, self.location[0], -1):
            v.append((i, self.location[1] + j))
            v.append((i, self.location[1] - j))
            j += 1
        return v

    def update_time(self, time):
        """
        :param crds_loc: A tuple representing the coords of the required location.
        :return: True upon success, False otherwise
        """
        self.time = time







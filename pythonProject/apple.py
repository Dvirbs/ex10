from typing import *
import game_parameters

class Apple:
    """
    Apple object
    """
    # TODO - check how we connect the color of the object Apple to the game_display
    Color = 'Green'

    def __init__(self):
        """
        A constructor for a Apple object
        :param location: A tuple representing the aplle (row, col) location
        """
        # check conditions if the inputs is correct
        self.__locatation = game_parameters.get_random_apple_data()[:-1] #(x,y)
        # TODO - maybe we will need to add the score as a field of the apple

    def movement_requirements(self) -> Tuple[int, int]:
        """
        check if coordinate that we want to move the apple is empty
        :return: A tuple of cell locations which must be empty in order for this move to be legal.
        """
        return game_parameters.get_random_apple_data()[:-1]         # (x,y)

    def update_location(self, move_key) -> bool:
        """
        update the location if it does
        :param move_key: A tuple representing the key of the required move.
        :return: True upon success, False otherwise
        """
        self.__locatation = move_key
        return




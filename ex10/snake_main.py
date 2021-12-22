import game_display
import game_parameters
import snake
from bomb import Bomb
import bomb
from snake import Snake
import apple
from typing import *

class Game:
    """
    the game snake that have 3 object snake, bomb abd apple.
    the target is to eat all the apples and get hight score with out crushing the bombs or board borders.
    """
    Hight = game_parameters.HEIGHT
    Width = game_parameters.WIDTH
    Apple_color = 'green'
    Snake_color = 'black'
    Bomb_color = 'red'
    Blast_color = 'orange'
    Number_of_bombs = 1
    INITIAL_SCORE = 0


    def __init__(self):
        """
        the game consrector with snake, bomb, apples and score
        """
        self.snake = Snake()  # TODO change to now see
        self.__bombs = []
        self.__apples = []
        self.__score = self.INITIAL_SCORE

    def in_board(self, x, y):
        """
        function that tell if we are in the board
        :param col: object row
        :param row: object row
        :return: True if in the board and False else
        """
        in_Width = -1 < x and x < self.Width
        in_Hight = -1 < y and y < self.Hight
        return in_Width and in_Hight

    def all_bombs_blasts(self) -> List[Tuple]:
        """
        list of all blast cells of all bumbs
        """
        all_blasts = list()
        for bomb in self.__bombs:
            if bomb.get_time() < 0:
                all_blasts += bomb.blast_cords()
        return all_blasts

    def cell_empty(self, x, y) -> bool:
        """
        check if cell is empty
        :param x: row number of object
        :param y: col number of object
        :return: True ig cell empty and False if not
        """
        all = []

        all += self.snake.get_locations()
        all += self.bomb_cells()
        all += [apple.get_location for apple in self.__apples]
        all += self.all_bombs_blasts()

        if (x, y) in all:
            return False
        return True

    def classifi(self, color):
        black_cells: List = list()
        red_cells: List = list()
        orange_cells: List = list()
        green_cells: List = list()
        # הפונקציה הזאת הייתה שוה לחלוטין ומחלוקת לפי פונקציות שונות אבל בגלל שהיה עניין של סדר בפריסומביט נאלצנו לכתוב כך
        # classifi the snake
        for loc in self.snake.get_locations():
            if loc in self.all_bombs_blasts():
                orange_cells.append((loc[0], loc[1]))
            elif loc in self.bomb_cells():
                red_cells.append((loc[0], loc[1]))
            else:
                black_cells.append((loc[0], loc[1]))
        # classifi the bomb

        for bomb in self.get_bombs():
            if bomb.get_time() > 0:
                bomb_row = bomb.get_location()[0]
                bomb_col = bomb.get_location()[1]
                red_cells.append((bomb_row, bomb_col))
            else:
                blast_cords_list = bomb.blast_cords()
                for blast_row, blast_col in blast_cords_list:
                    if self.in_board(blast_row, blast_col):
                        orange_cells.append((blast_row, blast_col))

        # cllasifi the apple

        for apple_row, apple_col in self.apples_cells():
            green_cells.append((apple_row, apple_col))

        # return condition
        if color == self.Bomb_color:
            return red_cells
        elif color == self.Blast_color:
            return orange_cells
        elif color == self.Snake_color:
            return black_cells
        else:
            return green_cells



    def draw_cell(self,gd,color_cells_list, color) -> None:
        """
        draw the cells by there colors of diffrent objects
        :param gd: game display parmater
        :return: None
        """
        for cell in color_cells_list:
            x = cell[0]
            y = cell[1]
            gd.draw_cell(x, y, color)

    ##### snake part  #####

    def get_snake(self) -> Snake:
        return self.snake

    def set_initial_snake(self) -> None:
        self.snake.add_new_head((10, 8))
        self.snake.add_new_head((10, 9))
        self.snake.add_new_head((10, 10))


    def eat_apple(self, tail) -> None:
        self.snake.add_to_tail(tail)

    ####### Bomb part  #########

    def get_bombs(self) -> List[Bomb]:
        return self.__bombs

    def add_bombs(self) -> None:
        while len(self.__bombs) < self.Number_of_bombs:
            bomb: Bomb = Bomb()
            bomb.set_bomb()
            x, y = bomb.get_location()
            if self.cell_empty(x, y) and self.in_board(x, y):
                self.__bombs.append(bomb)

    def bomb_cells(self) -> List[Tuple]:
        bomb_list = list()
        for bomb in self.__bombs:
            bomb_list.append(bomb.get_location())
        return bomb_list

    def remove_bomb(self, bomb: Bomb) -> None:
        self.__bombs.remove(bomb)

    ######## apple part  #########

    def get_apple_by_cord(self, apple_cords):
        """
        get the apple object by his cords
        :param apple_cords:
        :return: the apple
        """
        for apple in self.__apples:
            if apple_cords == apple.get_location():
                return apple

    def set_score(self, score) -> None:
        self.__score += score

    def get_score(self) -> int:
        return self.__score

    def apples_list(self):
        return self.__apples

    def remove_apple(self, apple) -> None:
        self.__apples.remove(apple)

    def add_apples(self) -> None:
        """
        function that sets 3 apple in self.__apples
        :return: None
        """
        while len(self.__apples) < 3:
            iphon: Apple = apple.Apple()
            iphon.set_apple()
            iphon.set_color(self.Apple_color)
            (x, y) = iphon.get_location()
            if self.cell_empty(x, y) and self.in_board(x,
                                                       y):  # TODO function that collactiong the snake and bomb cells
                self.__apples.append(iphon)

    def apples_cells(self) -> List[Tuple]:
        """
        :return: return apples cells
        """
        apples_list = list()
        for apple in self.__apples:
            apple_row = apple.get_location()[0]
            apple_col = apple.get_location()[1]
            apples_list.append((apple_row, apple_col))
        return apples_list



def main_loop(gd) -> None:
    """
    the main function that connect all the objects and run the game
    :param gd: game parameters
    :return:None
    """
    # initial properties
    game = Game()
    game.set_initial_snake()
    game.add_bombs()
    gd.show_score(game.get_score())
    game.add_apples()
    snake_increase = 0
    tail = None
    another_loop = True

    # draw the cells
    game.draw_cell(gd, game.classifi(game.Snake_color), game.Snake_color)
    game.draw_cell(gd, game.classifi(game.Bomb_color), game.Bomb_color)
    game.draw_cell(gd, game.classifi(game.Blast_color), game.Blast_color)
    game.draw_cell(gd, game.classifi(game.Apple_color), game.Apple_color)

    gd.end_round()
    while another_loop:
        snake = game.get_snake()
        apples = game.apples_list()
        bombs = game.get_bombs()

        # snake move
        key_clicked = gd.get_key_clicked()
        if key_clicked:
            snake.set_orientation(key_clicked)
        if snake_increase > 0 and tail:
            game.eat_apple(tail)
            snake_increase -= 1
        tail = snake.move()

        # check if snake run into himself
        if snake.get_head() in snake.get_locations()[1:]:
            another_loop = False

        # check if the snake run into bomb
        for bomb in bombs:
            bomb.time_getting_smaller()
            if -bomb.get_time() == bomb.get_redius():
                game.remove_bomb(bomb)
            if snake.get_head() == bomb.get_location():
                another_loop = False

        # check if the snake get out of board
        if not game.in_board(snake.get_head()[0], snake.get_head()[1]):
            snake.remove_head()
            another_loop = False

        # check if snake eat an apple
        for apple in apples:
            if snake.get_head() == apple.get_location():
                snake_increase += 3
                game.set_score(apple.get_score())
                game.remove_apple(apple)
                game.add_apples()

        # check if snake tuch the blasts
        if set(snake.get_locations()) & set(game.all_bombs_blasts()):
            another_loop = False

        #check if apple fall on fire bomb
        problamtic_apple_list = set(game.apples_cells()) & set(game.all_bombs_blasts())
        for problamtic_apple in problamtic_apple_list:
            if problamtic_apple:
                apple = game.get_apple_by_cord(tuple(problamtic_apple))
                game.remove_apple(apple)

        # add game objects
        gd.show_score(game.get_score())
        game.add_apples()

        # draw cells
        game.draw_cell(gd, game.classifi(game.Apple_color), game.Apple_color)
        game.draw_cell(gd, game.classifi(game.Snake_color), game.Snake_color)
        game.draw_cell(gd, game.classifi(game.Bomb_color), game.Bomb_color)
        game.draw_cell(gd, game.classifi(game.Blast_color), game.Blast_color)

        # add game objects
        game.add_bombs()

        gd.end_round()
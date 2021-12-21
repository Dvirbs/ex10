import game_display
import game_parameters
import snake
from game_display import GameDisplay
from bomb import Bomb
import bomb
from snake import Snake
import apple
from typing import *


class Game:
    Hight = game_parameters.HEIGHT
    Width = game_parameters.WIDTH
    Apple_color = 'green'  # TODO האם צריך לרשום את זה מחוץ לאינט או בתוכו
    Snake_color = 'Black'
    Bomb_color = 'red'

    def __init__(self):
        self.snake = Snake()  # TODO change to now see
        self.__bombs = []
        self.__apples = []
        self.__score = 0

    def get_bombs(self):
        return self.__bombs


    def set_score(self, score) -> None:
        self.__score += score

    def get_score(self) -> int:
        return self.__score

    def get_snake(self):
        return self.snake

    def apples_list(self):
        return self.__apples

    def remove_apple(self, apple) -> None:
        self.__apples.remove(apple)

    def set_initial_snake(self) -> None:
        self.snake.add_new_head((10, 10))
        self.snake.add_new_head((9, 10))
        self.snake.add_new_head((8, 10))

    def in_board(self, row, col):
        """
        function that tell if we are in the board
        :param col: object row
        :param row: object row
        :return: True if in the board and False else
        """
        in_rows = row < self.Hight
        in_columns = col < self.Width
        return in_rows and in_columns

    def add_apples(self) -> None:
        """
        function that sets 3 apple in self.__apples
        :return: None
        """
        while len(self.__apples) < 3:
            iphon: Apple = apple.Apple()
            iphon.set_apple()
            iphon.set_color(self.Apple_color)
            (row, col) = iphon.get_location()
            if self.cell_empty(row, col) and self.in_board(row,
                                                           col):  # TODO function that collactiong the snake and bomb cells
                self.__apples.append(iphon)

    def cell_empty(self, row, col) -> bool:
        """
        check if cell is empty
        :param row: row number of object
        :param col: col number of object
        :return: True ig cell empty and False if not
        """
        snake_cords: List = self.snake.get_locations()
        bombs_cords: List[Tuple] = self.bomb_cells()
        apple_cords: List = [apple.get_location for apple in self.__apples]
        all = []
        all += snake_cords
        all += bombs_cords
        all += apple_cords
        if (row, col) in all:
            return False
        return True

    def add_bombs(self) -> None:
        while len(self.__bombs) <3:
            bomb: Bomb = Bomb()
            bomb.set_bomb()
            row, col = bomb.get_location()
            if self.cell_empty(row, col) and self.in_board(row, col):
                self.__bombs.append(bomb)

    # def add_bombs(self) -> None:
    #     """המתודה מריצה פצצות באופן רנדומלי ואם הם מתאימות היא מכניסה אותן ל self.bombs.
    #     הלולאה נעצרת כאשר יש 3 פצצות ברשימה.
    #     """
    #     while len(self.__bombs) < 3:
    #         lst_bomb_data = list(game_parameters.get_random_bomb_data())  # הכנסת המידע לתוך רשימה
    #         row = lst_bomb_data[1]
    #         col = lst_bomb_data[0]
    #         # בדיקה האם הפצצה מתאימה למשחק
    #         if self.cell_empty(row, col) and self.in_board(row, col):
    #             redius = lst_bomb_data[2]
    #             time = lst_bomb_data[3]
    #             self.__bombs.append(bomb.Bomb((row, col), redius, time ))

    def bomb_cells(self) -> List[Tuple]:
        bomb_list = list()
        for bomb in self.__bombs:
            bomb_list.append(bomb.get_location())
        return bomb_list

    # def bomb_cells(self) -> Tuple[List,List]:
    #     "מחזירה רשימה של תאים בהם מופיעות פצצות או גלי הדף"
    #     bomb_cells = []
    #     blast_cells = []
    #
    #     for bomb in self.__bombs:
    #         if bomb.time <= 0:  # saving the blast waves when the time is finish
    #             blast_cells += bomb.coordinates_by_radius(bomb.time)
    #             #saving the bomb location before time is finish
    #         else: #TODO check if we can להגריל bomb in the same location of the bomb that  couse the blast on the board
    #             bomb_cells.append(bomb.location)
    #     return bomb_cells, blast_cells

    def move_snake(self):
        """
        moves snake one step in given direction.
        :param movekey: Key of move in snake to activate
        :return: True upon success, False otherwise
        """
        tail = self.snake.move()
        row_head = self.snake.get_head()[0]
        col_head = self.snake.get_head()[1]
        # בדיקה האם הנחש הגיע לתא שנמצא ברשימה השחורה או אם חרג מהלוח
        if (row_head, col_head) in self.bomb_cells() or \
                row_head > game_parameters.HEIGHT or col_head > game_parameters.WIDTH:
            return
        return tail

    def eat_apple(self, tail):
        self.snake.add_to_tail(tail)

    def draw(self, gd):
        for loc in self.snake.get_locations():
            gd.draw_cell(loc[0], loc[1], self.Snake_color)
        for apple_row, apple_col in self.apples_cells():
            gd.draw_cell(apple_row, apple_col, self.Apple_color)
        for bomb_row, bomb_col in self.bomb_cells():
            gd.draw_cell(bomb_row, bomb_col, self.Bomb_color)


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


def main_loop(gd: GameDisplay) -> None:
    game = Game()
    game.set_initial_snake()
    game.add_bombs()
    gd.show_score(game.get_score())
    game.add_apples()
    count_increase = 0
    tail = None
    while True:
        key_clicked = gd.get_key_clicked()
        if key_clicked:
            game.snake.set_orientation(key_clicked)
        if count_increase > 0 and tail:
            game.eat_apple(tail)
            count_increase -= 1
        tail = game.move_snake()
        # check if snake run into himself
        if game.snake.get_head() in game.snake.get_locations()[1:]:
            # TODO board with game over
            break

        # check if the snake run into bomb
        for bomb in game.get_bombs():
            if game.snake.get_head() == bomb.get_location():
                # TODO draw the bomb on the board
                return

        # apple part
        for apple in game.apples_list():
            if game.snake.get_head() == apple.get_location():
                count_increase += 3
                game.set_score(apple.get_score())
                game.remove_apple(apple)

        gd.show_score(game.get_score())
        game.draw(gd)
        game.add_apples()

        gd.end_round()

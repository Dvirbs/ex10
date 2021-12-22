import game_display
import game_parameters
import snake
from game_display import GameDisplay
from bomb import Bomb
import bomb
from snake import Snake
import apple
from typing import *
import time  #only for tests


class Game:
    Hight = game_parameters.HEIGHT
    Width = game_parameters.WIDTH
    Apple_color = 'green'  # TODO האם צריך לרשום את זה מחוץ לאינט או בתוכו
    Snake_color = 'Black'
    Bomb_color = 'red'
    Blast_color = 'orange'

    def __init__(self):
        self.snake = Snake()  # TODO change to now see
        self.__bombs = []
        self.__apples = []
        self.__score = 0

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
        snake_cords: List = self.snake.get_locations()
        bombs_cords: List[Tuple] = self.bomb_cells()
        apple_cords: List = [apple.get_location for apple in self.__apples]
        blast_cords: List = self.all_bombs_blasts()
        all = []
        all += snake_cords
        all += bombs_cords
        all += apple_cords
        all += blast_cords
        if (x, y) in all:
            return False
        return True

    def draw(self, gd):
        for loc in self.snake.get_locations():
            gd.draw_cell(loc[0], loc[1], self.Snake_color)
        for apple_row, apple_col in self.apples_cells():
            gd.draw_cell(apple_row, apple_col, self.Apple_color)
        for bomb in self.get_bombs():
            if bomb.get_time() >= 0:
                bomb_row = bomb.get_location()[0]
                bomb_col = bomb.get_location()[1]
                gd.draw_cell(bomb_row, bomb_col, self.Bomb_color)
            else:
                blast_cords_list = bomb.blast_cords()
                for blast_row, blast_col in blast_cords_list:
                    if self.in_board(blast_row, blast_col):
                        gd.draw_cell(blast_row, blast_col, self.Blast_color)

    ##### snake part  #####

    def get_snake(self):
        return self.snake

    def set_initial_snake(self) -> None:
        self.snake.add_new_head((10, 10))
        self.snake.add_new_head((9, 10))
        self.snake.add_new_head((8, 10))

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

    ####### Bomb part  #########

    def get_bombs(self):
        return self.__bombs

    def add_bombs(self) -> None:
        while len(self.__bombs) < 1:
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


def main_loop(gd: GameDisplay) -> None:
    game = Game()
    game.set_initial_snake()
    game.add_bombs()
    gd.show_score(game.get_score())
    game.add_apples()
    count_increase = 0
    tail = None
    while True:
        time.sleep(0.5)  #every loop slow the time for check test
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
            bomb.time_getting_smaller()

            if -bomb.get_time() == bomb.get_redius():
                game.remove_bomb(bomb)

            if game.snake.get_head() == bomb.get_location():
                # TODO draw the big bomb on the board
                return
        if set(game.snake.get_locations()) & set(game.all_bombs_blasts()):
            return

        # apple part
        for apple in game.apples_list():
            if game.snake.get_head() == apple.get_location():
                count_increase += 3
                game.set_score(apple.get_score())
                game.remove_apple(apple)

        gd.show_score(game.get_score())
        game.draw(gd)
        game.add_bombs()
        game.add_apples()

        gd.end_round()

# 78 Function call: GameDisplay(456,['Left', None, None, 'Down', 'Right', None, 'Up', 'Left', None, None, None, 'Up', 'Right', 'Down'],79
# Expected return value: [(0, {(10, 10): 'black', (10, 9): 'black', (10, 8): 'black', (9, 10): 'red', (37, 9): 'green', (25, 29): 'green', (10, 27): 'green'}),
#                         (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (10, 11): 'black', (10, 10): 'black', (10, 9): 'black', (9, 10): 'red'}),
#                         (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (10, 12): 'black', (10, 11): 'black', (10, 10): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (10, 13): 'black', (10, 12): 'black', (10, 11): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (10, 14): 'black', (10, 13): 'black', (10, 12): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (10, 15): 'black', (10, 14): 'black', (10, 13): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (10, 16): 'black', (10, 15): 'black', (10, 14): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (10, 17): 'black', (10, 16): 'black', (10, 15): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (10, 18): 'black', (10, 17): 'black', (10, 16): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (10, 19): 'black', (10, 18): 'black', (10, 17): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (9, 19): 'black', (10, 19): 'black', (10, 18): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (8, 19): 'black', (9, 19): 'black', (10, 19): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (7, 19): 'black', (8, 19): 'black', (9, 19): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (7, 18): 'black', (7, 19): 'black', (8, 19): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (7, 17): 'black', (7, 18): 'black', (7, 19): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (7, 16): 'black', (7, 17): 'black', (7, 18): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (7, 15): 'black', (7, 16): 'black', (7, 17): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (7, 14): 'black', (7, 15): 'black', (7, 16): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (7, 13): 'black', (7, 14): 'black', (7, 15): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (7, 12): 'black', (7, 13): 'black', (7, 14): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (7, 11): 'black', (7, 12): 'black', (7, 13): 'black', (9, 10): 'red'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (7, 10): 'black', (7, 11): 'black', (7, 12): 'black', (9, 10): 'orange'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (7, 9): 'black', (7, 10): 'black', (7, 11): 'black', (9, 11): 'orange', (8, 10): 'orange', (9, 9): 'orange', (10, 10): 'orange'}), (0, {(37, 9): 'green', (25, 29): 'green', (10, 27): 'green', (7, 8): 'black', (7, 9): 'black', (7, 10): 'orange', (9, 12): 'orange', (10, 11): 'orange', (8, 11): 'orange', (9, 8): 'orange', (8, 9): 'orange', (11, 10): 'orange', (10, 9): 'orange'})]
import game_display
import game_parameters
import snake
from game_display import GameDisplay
import bomb
from snake import Snake
import apple
from typing import *


class Game:
    Hight = game_parameters.HEIGHT
    Width = game_parameters.WIDTH
    Apple_color = 'green'  # TODO האם צריך לרשום את זה מחוץ לאינט או בתוכו
    Snake_color = 'Black'

    def __init__(self):
        self.snake = Snake() #TODO change to now see
        self.__bombs = []
        self.__apples = []
        self.__score = 0

    def set_score(self, score) -> None:
        self.__score += score

    def get_score(self) -> int:
        return self.__score

    def get_snake(self):
        return self.snake

    def get_apples(self):
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
        bombs_cords: List = self.bomb_cells
        apple_cords: List = [apple.get_location for apple in self.__apples]
        all = []
        all += snake_cords
        all += apple_cords
        # all += bombs_cords #TODO
        if (row, col) in all:
            return False
        return True

    def cell_is_empty(self, coordinate):
        """בעיקרון המחשבה הייתה לסמן תאים ריקים כאפסים, תאי נחש - 1, תאי פצצה - 2, תאי הדף- 3"""
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: num of object if their is object in coordinate, True if empty
        """
        # TODO לבנות פונקציה אחרת שנונת את הקורדינטות התפוסות
        if self.board[list(coordinate)[0]][list(coordinate)[1]] == 0:
            return True
        return self.board[list(coordinate)[0]][list(coordinate)[1]]

    def add_bombs(self) -> None:
        """המתודה מריצה פצצות באופן רנדומלי ואם הם מתאימות היא מכניסה אותן ל self.bombs.
        הלולאה נעצרת כאשר יש 3 פצצות ברשימה.
        """
        while len(self.bombs) < 3:
            lst_bomb_data = list(game_parameters.get_random_bomb_data())  # הכנסת המידע לתוך רשימה
            row = lst_bomb_data[1]
            col = lst_bomb_data[0]
            # בדיקה האם הפצצה מתאימה למשחק
            if self.cell_is_empty((row, col)) and row < game_parameters.HEIGHT or col < game_parameters.WIDTH:
                self.board[row][col] = 2
                self.bombs.append(bomb.Bomb((row, col), lst_bomb_data[2], lst_bomb_data[3]))

    def bomb_cells(self) -> list:
        "מחזירה רשימה של תאים בהם מופיעות פצצות או גלי הדף"
        lst_cells = []
        for bomb in self.__bombs:
            if bomb.time <= 0:  # לזכור שבזמן הזה הטיים ז מינוס.. לא לשכוח להתייחס לזה
                lst_cells += bomb.coordinates_by_radius(bomb.time)
            else:
                lst_cells.append(bomb.location)
            lst_cells.append += self.snake.move()[0:]
        return lst_cells

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
    gd.show_score(game.get_score())
    game.set_initial_snake()
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

        if game.snake.get_head() in game.snake.get_locations()[1:]:
            #TODO board with game over
            break

        # apple part
        for apple in game.get_apples():
            if game.snake.get_head() == apple.get_location():
                count_increase += 3
                game.set_score(apple.get_score())
                game.remove_apple(apple)

        gd.show_score(game.get_score())
        game.draw(gd)
        game.add_apples()

        gd.end_round()

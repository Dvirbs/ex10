import game_display
import game_parameters
from game_display import GameDisplay
import bomb
from snake import Snake


class Game:
    def __init__(self):
        bd = []
        for i in range(game_parameters.HEIGHT):
            bd.append([])
            for j in range(game_parameters.WIDTH):
                bd[i].append(0)
            self.board = bd
            self.snake = Snake()
            self.bombs = []

    def cell_is_empty(self, coordinate):
        """בעיקרון המחשבה הייתה לסמן תאים ריקים כאפסים, תאי נחש - 1, תאי פצצה - 2, תאי הדף- 3"""
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: num of object if their is object in coordinate, True if empty
        """
        if self.board[list(coordinate)[0]][list(coordinate)[1]] == 0:
            return True
        return self.board[list(coordinate)[0]][list(coordinate)[1]]

    def add_bombs(self) -> None:
        """המתודה מריצה פצצות באופן רנדומלי ואם הם מתאימות היא מכניסה אותן ל self.bombs.
        הלולאה נעצרת כאשר יש 3 פצצות ברשימה.
        """
        while len(self.bombs) < 3:
            lst_bomb_data = list(game_parameters.get_random_bomb_data()) # הכנסת המידע לתוך רשימה
            row = lst_bomb_data[1]
            col = lst_bomb_data[0]
            # בדיקה האם הפצצה מתאימה למשחק
            if self.cell_is_empty((row, col)) and row < game_parameters.HEIGHT or col < game_parameters.WIDTH:
                self.board[row][col] = 2
                self.bombs.append(bomb.Bomb((row, col), lst_bomb_data[2], lst_bomb_data[3]))

    def bad_cells(self) -> list:
        "מחזירה רשימה של תאים בהם מופיעות פצצות או גלי הדף"
        lst_cells = []
        for bomb in self.bombs:
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
        if (row_head, col_head) in self.bad_cells() or \
                row_head > game_parameters.HEIGHT or col_head > game_parameters.WIDTH:
            return
        return tail


    def eat_apple(self, tail):
        self.snake.add_to_tail(tail)


def main_loop(gd: GameDisplay) -> None:
    gd.show_score(0)
    game = Game()
    game.snake.add_new_head((10,10))
    game.snake.add_new_head((9,10))
    game.snake.add_new_head((8,10))

    count_apple = 0
    tail = None
    while True:
        key_clicked = gd.get_key_clicked()
        if key_clicked:
            game.snake.set_orientation(key_clicked)
        if count_apple > 0 and tail:
            game.eat_apple(tail)
            count_apple -= 1
        tail = game.move_snake()
        if game.snake.get_head() == (20,9) or game.snake.get_head()==(22,9):
            count_apple += 3
        for loc in game.snake.get_location():
            gd.draw_cell(loc[0], loc[1], "Black")
        gd.draw_cell(20, 9, "green")
        gd.draw_cell(22, 9, "green")
        gd.end_round()
from node import Node

class Snake:
    def __init__(self):
        self.__head: Node = None
        self.__tail: None
        self.__length = 0
        self.__color = None
        self.__move_direcation = 'Right'
        self.__locations = []


    def add_new_head(self, new_head: Node) -> None:
        """מתודה שמוסיפה חוליה לראש הנחש ומתעדכנת להיות הראש החדש
               אם הנחש עוד לא הוגדר אז כעת הנחש יוגדר באורך 1 וראשו יהיה החוליה שבקלט"""

        self.__length += 1
        if self.__head is None:
            self.__head = new_head
            self.__tail = new_head
        else:
            new_head.set_prev(self.__head)
            self.__head.set_next(new_head)
            self.__head = self.__head.get_next()
        self.__locations.append(self.__head.get_data())

    # def add_tail(self, new_head: Node) -> None:
    #     self.__length += 1
    #     self.__tail = 5

    def get_location(self):
        return self.__locations

    def get_head(self) -> Node:
        return self.__head

    def get_tail(self) -> Node:
        return self.__tail

    def remove_tail(self):
        self.__length -= 1
        self.__tail = self.__tail.get_next()
        self.__tail.get_prev().set_next(None)
        self.__tail.set_prev(None)

    def set_color(self, color: str):
        self.__color = color

    def possible_moves(self):
        """מחזירה על סמך הכיוון הנוכחי של הנחש מהם המהלכים האפשריים"""
        if self.__orientation == "Right":
            return ["Down", "Up"]
        if self.__orientation == "Left":
            return ["Down", "Up"]
        if self.__orientation == "Up":
            return ["Right", "Left"]
        if self.__orientation == "Down":
            return ["Right", "Left"]

    def set_orientation(self, movekey):
        possible_move = self.possible_moves()
        if movekey in possible_move:  # אם הכיוון נמצא ברשימת הכיוונים - נעדכן את הכיוון.
            self.__orientation = movekey

    def move(self):
        """פונקציה המקבלת כיוון ומחזירה אמת אם הנחש זז בהצלחה, שקר אחרת"""
        row_head = self.get_head().get_data()[0]
        col_head = self.get_head().get_data()[1]

        if self.__orientation == "Right":
            x = row_head
            y = col_head + 1
        elif self.__orientation == "Left":
            x = row_head
            y = col_head - 1
        elif self.__orientation == "Down":
            x = row_head + 1
            y = col_head
        else:
            x = row_head - 1
            y = col_head
        if self.in_crash((x, y)):  # אם הראש העתידי של הנחש יפגע בגופו נחזיר False
             return False
        new_head = Node((x, y))
        self.add_new_head(new_head)
        print(self.get_location())
        self.remove_tail()
        print(self.get_location())
        return True

s = Snake()
head = Node((7,10))
s.add_new_head(head)
head = Node((7,11))
s.add_new_head(head)

print(s.get_head().get_data())
print(s.get_tail().get_data())
head = Node((7,12))
s.add_new_head(head)
print(s.get_head().get_data())
print(s.get_tail().get_data())
s.remove_tail()
print(s.get_head().get_data())
print(s.get_tail().get_data())
# print(s.get_location())


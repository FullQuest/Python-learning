from tkinter import Tk, Frame
import random
import time

def __set_key(e, root):
    """
    e - event with attribute 'char', the released key
    """
    global key_pressed
    if e.char:
        key_pressed = e.char
        root.destroy()


# function to get input without confirm with "enter" key.
# Got it from here: https://stackoverflow.com/questions/3523174/raw-input-without-pressing-enter
def get_key(time_to_sleep=3, msg=""):
    """
    msg - set to empty string if you don't want to print anything
    time_to_sleep - default 3 seconds
    """
    global key_pressed
    if msg:
        print(msg)
    key_pressed = None
    root = Tk()
    root.overrideredirect(True)
    frame = Frame(root, width=0, height=0)
    frame.bind("<KeyRelease>", lambda f: __set_key(f, root))
    frame.pack()
    root.focus_set()
    frame.focus_set()
    frame.focus_force()  # doesn't work in a while loop without it
    root.after(time_to_sleep * 9999, func=root.destroy)
    root.mainloop()
    root = None  # just in case
    return key_pressed


# part of validate input. Input itself.
def user_input(possible_values):
    key = None
    while key not in possible_values:
        key = get_key(2)
    return key


class Deck:
    screen_background_symbol = "•"

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = [[self.screen_background_symbol for x in range(width)] for y in range(height)]

    def show(self):
        screen_output = ''
        for row_num in range(self.height):
            row = ''.join(self.screen[row_num])
            screen_output += row + "\n"
        print('\n\n\n\n\n\n\n\n')
        print(screen_output)
        self.screen = [[self.screen_background_symbol for x in range(self.width)] for y in range(self.height)]

    def update_snake(self, snake):
        for coord in snake.coordinates:
            self.screen[coord[0]][coord[1]] = snake.snake_symbol


class Snake:
    snake_symbol = '@'
    directions_possible = ['Up', 'Right', 'Down', 'Left']
    directions_dict = {'Up': 0, 'Right': 1, 'Down': 2, 'Left': 3}

    def __init__(self, deck_width, deck_height):
        self.length = 1
        # self.cur_direction = self.directions_possible[random.randint(0, 3)]
        self.cur_direction = self.directions_possible[3]
        # self.coordinates = [deck_width // 2, deck_height // 2]
        self.coordinates = [[deck_height // 2, deck_width // 2], [2, 9], [2, 10], [3, 10], [3, 11],
                            [3, 12], [3, 13]]

    def valid_directions(self):
        numeric_cur_directions = self.directions_dict[self.cur_direction]
        wrong_vector = None

        if numeric_cur_directions > 1:
            wrong_vector = numeric_cur_directions - 2
        else:
            wrong_vector = numeric_cur_directions + 2

        # Get key by value
        wrong_vector_key = list(self.directions_dict.keys())[list(self.directions_dict.values()).index(wrong_vector)]

        return [vector for vector in self.directions_possible if vector != wrong_vector_key]

    def get_head_move_coord(self, vector):
        head_coord = self.coordinates[0]
        if vector == 'Up':
            return [head_coord[0] - 1, head_coord[1]]
        if vector == 'Down':
            return [head_coord[0] + 1, head_coord[1]]
        if vector == 'Left':
            return [head_coord[0], head_coord[1] - 1]
        if vector == 'Right':
            return [head_coord[0], head_coord[1] + 1]

    def move(self, snake_move_direction, on_eat=False):
        if not on_eat:
            self.coordinates.pop()

        if snake_move_direction not in self.valid_directions():
            snake_move_direction = self.cur_direction

        self.cur_direction = snake_move_direction

        self.coordinates.insert(0, self.get_head_move_coord(snake_move_direction))


def update_screen():
    my_deck.update_snake(my_snake)
    my_deck.show()


possible_input_values = ['w', 'd', 's', 'a', 'j']
directions_input = {'w': "Up", 'd': "Right", 's': "Down", 'a': "Left"}

deck_width = 16
deck_height = 5

my_deck = Deck(deck_width, deck_height)
my_snake = Snake(deck_width, deck_height)

update_screen()

game_on = True
while game_on:
    user_key = user_input(possible_input_values)
    if user_key == "j":
        game_on = False
        break

    my_snake.move(directions_input[user_key])
    update_screen()

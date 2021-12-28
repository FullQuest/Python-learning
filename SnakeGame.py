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
    wall_symbol = "#"

    def __init__(self, width=8, height=8, screen_background_symbol=" "):
        if width not in range(4, 20):
            width = 8
        if height not in range(4, 20):
            height = 8

        self.screen_background_symbol = screen_background_symbol
        self.width = width
        self.height = height
        self.screen = [[self.screen_background_symbol for x in range(width)] for y in range(height)]

    def show(self):
        screen_output = (self.wall_symbol * 2) + (self.wall_symbol * self.width)
        for row_num in range(self.height):

            if screen_output != "":
                screen_output += '\n'

            row = ''.join(self.screen[row_num])
            screen_output += self.wall_symbol + row + self.wall_symbol

        screen_output += '\n' + (self.wall_symbol * 2) + (self.wall_symbol * self.width)
        print(screen_output)
        self.screen = [[self.screen_background_symbol for x in range(self.width)] for y in range(self.height)]

    def update_screen_objects(self, snake_object, food_object):

        for coord in snake_object.coordinates:
            # print(coord)
            # print(self.screen)
            # print(self.screen[8])
            self.screen[coord[0]][coord[1]] = snake_object.snake_symbol

        self.screen[food_object.position[0]][food_object.position[1]] = food_object.food_symbol


class Snake:
    snake_symbol = '@'
    directions_possible = ['Up', 'Right', 'Down', 'Left']
    directions_dict = {'Up': 0, 'Right': 1, 'Down': 2, 'Left': 3}

    def __init__(self, deck_width, deck_height):
        self.length = 1
        self.cur_direction = self.directions_possible[random.randint(0, 3)]
        # self.cur_direction = self.directions_possible[3]
        self.coordinates = [[deck_height // 2, deck_width // 2]]
        # self.coordinates = [[deck_height // 2, deck_width // 2], [2, 9]]

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

    def get_head_move_coord(self, direction):

        if direction not in self.valid_directions():
            direction = self.cur_direction

        self.cur_direction = direction

        head_coord = self.coordinates[0]
        if direction == 'Up':
            return [head_coord[0] - 1, head_coord[1]]
        if direction == 'Down':
            return [head_coord[0] + 1, head_coord[1]]
        if direction == 'Left':
            return [head_coord[0], head_coord[1] - 1]
        if direction == 'Right':
            return [head_coord[0], head_coord[1] + 1]

    def move(self, snake_move_direction, on_eat=False):

        self.coordinates.insert(0, self.get_head_move_coord(snake_move_direction))

        if not on_eat:
            self.coordinates.pop()


class Food:

    def __init__(self, occupied_coordinates, deck_width, deck_height, food_symbol="$"):
        self.food_symbol = food_symbol
        self.deck_width = deck_width
        self.deck_height = deck_height
        self.occupied_coordinates = occupied_coordinates

        all_coordinates = []

        for i in range(self.deck_height):
            for j in range(self.deck_width):
                all_coordinates += [[i, j]]

        possible_coordinates = [coord for coord in all_coordinates if coord not in self.occupied_coordinates]

        self.position = random.choice(possible_coordinates)


def update_screen(score):
    my_deck.update_screen_objects(my_snake, food_peace)
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    my_deck.show()
    print(f'Current score: {score}')


# deck_width = 16
# deck_height = 5
#
# my_snake = Snake(deck_width, deck_height)
# my_deck = Deck(deck_width, deck_height)
#
# food_test = Food(my_snake.coordinates, deck_width, deck_height)
# print(food_test.position)
#
# my_deck.update_screen_objects(my_snake, food_test)
# my_deck.show()


possible_input_values = ['w', 'd', 's', 'a', 'j']
directions_input = {'w': "Up", 'd': "Right", 's': "Down", 'a': "Left"}

deck_width = 16
deck_height = 5

# valid coords for walls collision check
valid_coordinates = []
for i in range(deck_height):
    for j in range(deck_width):
        valid_coordinates += [[i, j]]

my_deck = Deck(deck_width, deck_height)
my_snake = Snake(deck_width, deck_height)
food_peace = Food(my_snake.coordinates, deck_width, deck_height)
score = 0

update_screen(score)
on_eat = False

game_on = True
while game_on:

    # get input key from user
    user_key = user_input(possible_input_values)

    # "j" is exit input for break snake game
    if user_key == "j":
        game_on = False
        break

    # stop game on wall collision
    if my_snake.get_head_move_coord(directions_input[user_key]) not in valid_coordinates:
        game_on = False
        print(f'The game is over, the wall was stronger. Your score is {score}!')
        break

    # check if snake eats the food. If it does than on_eat = true
    if my_snake.get_head_move_coord(directions_input[user_key]) == food_peace.position:
        on_eat = True

    # move snake
    my_snake.move(directions_input[user_key], on_eat)

    # recreate food object if one before was eaten
    if on_eat:
        score += 1
        food_peace = Food(my_snake.coordinates, deck_width, deck_height)
        on_eat = False

    # show updated screen
    update_screen(score)

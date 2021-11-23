from tkinter import Tk, Frame


def __set_key(e, root):
    """
    e - event with attribute 'char', the released key
    """
    global key_pressed
    if e.char:
        key_pressed = e.char
        root.destroy()


def get_key(time_to_sleep=3, msg=""):
    """
    msg - set to empty string if you don't want to print anything
    time_to_sleep - default 3 seconds
    SOURCE https://stackoverflow.com/questions/42650289/split-an-array-dependent-on-the-array-values-in-python
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


def user_input(possible_values):
    key = None
    while key not in possible_values + ['j']:
        key = get_key(2)
    return key


def update_screen(screen):
    # just for make an illusion of screen update
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print(screen[0:3])
    print(screen[3:6])
    print(screen[6:9])


def validate_input(players, screen, possible_values, current_player):
    input = key_to_index[user_input(possible_values)]
    screen[input] = players[current_player]

    return [screen, input]


num_input_static = ["7", "8", "9", "4", "5", "6", "1", "2", "3"]
lowercase_input_static = ["q", "w", "e", "a", "s", "d", "z", "x", "c"]
num_input = num_input_static
lowercase_input = lowercase_input_static
screen = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
players = {'1': 'X', '2': 'O'}
key_to_index = {"7": 0, "8": 1, "9": 2, "4": 3, "5": 4, "6": 5, "1": 6, "2": 7, "3": 8,
                "q": 0, "w": 1, "e": 2, "a": 3, "s": 4, "d": 5, "z": 6, "x": 7, "c": 8}


update_screen(screen)

current_player = '1'
possible_values = num_input+lowercase_input

for i in range(9):
    valimp = validate_input(players, screen, possible_values, current_player)
    screen = valimp[0]
    exclude_val = valimp[1]

    update_screen(screen)

    num_input[exclude_val] = 0
    lowercase_input[exclude_val] = 0


    possible_values = num_input+lowercase_input

    if current_player == '1':
        current_player = '2'
    else:
        current_player = '1'


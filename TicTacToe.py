from tkinter import Tk, Frame


def __set_key(e, root):
    """
    e - event with attribute 'char', the released key
    """
    global key_pressed
    if e.char:
        key_pressed = e.char
        root.destroy()


# function to get input without confirm with "enter" key.
# Got it from here: https://stackoverflow.com/questions/42650289/split-an-array-dependent-on-the-array-values-in-python
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


# show current screen
def update_screen(screen, current_player):
    # just for make an illusion of screen update
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print(f'Use numpad or "qweasdzxc" as an input. Current move is {current_player}')
    print(screen[0:3])
    print(screen[3:6])
    print(screen[6:9])


# part of validate input. Input itself.
def user_input(possible_values):
    key = None
    while key not in possible_values:
        key = get_key(2)
    return key


# Apply input only if it's in pre-defined possible_values. in this version also has info about player
# In future will get rid of it
def validate_input(players, screen, possible_values, current_player):
    input = key_to_index[user_input(possible_values)]
    screen[input] = players[current_player]

    return [screen, input]


# Check if screen has win combination with provided symbol
def has_three_in_row(screen, symbol):
    row = symbol * 3
    win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for combination in win_combinations:
        if ''.join(screen[combination[0]] + screen[combination[1]] + screen[combination[2]]) == row:
            return True
    return False


# possible input values.
num_input = ["7", "8", "9", "4", "5", "6", "1", "2", "3"]
lowercase_input = ["q", "w", "e", "a", "s", "d", "z", "x", "c"]

# Screen array
screen = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# player's signs that can be changed.
players = {'1': 'X', '2': 'O'}

# Dict to convert comfortable players input into it's index on screen
key_to_index = {"7": 0, "8": 1, "9": 2, "4": 3, "5": 4, "6": 5, "1": 6, "2": 7, "3": 8,
                "q": 0, "w": 1, "e": 2, "a": 3, "s": 4, "d": 5, "z": 6, "x": 7, "c": 8}

# pre-define start values
current_player = '1'
possible_values = num_input + lowercase_input

for i in range(9):

    update_screen(screen, players[current_player])
    # get valid player input
    valimp = validate_input(players, screen, possible_values, current_player)

    # show it on screen
    screen = valimp[0]

    # check for win
    if has_three_in_row(screen, players[current_player]):
        update_screen(screen, players[current_player])
        print(f'Player {current_player} win!')
        break

    # remove filled values from valid list
    exclude_val = valimp[1]
    num_input[exclude_val] = 0
    lowercase_input[exclude_val] = 0

    # update valid input values list (for next check)
    possible_values = num_input + lowercase_input

    # change current player
    if current_player == '1':
        current_player = '2'
    else:
        current_player = '1'

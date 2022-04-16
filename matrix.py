import random
matrix = []
matrix_ui = []
symbols = {-1: ('\u2588', '*'), 0: ('\u2588', ' '), 1: ('\u2588', 1), 2: ('\u2588', 2), 3: ('\u2588', 3), 4: ('\u2588', 4), 5: ('\u2588', 5), 6: ('\u2588', 6), 7: ('\u2588', 7), 8: ('\u2588', 8), '?': None}  # \u2588 means █, \u1F4A3 means Ὂ in unicode
def generate_matrix(): # Actual values
    for i in range(0, 9):
        matrix.append([])
        for j in range(0, 9):
            matrix[i].append(0)

def generate_matrix_interface(): # Displayed values
    for i in range(0, 9):
        matrix_ui.append([])
        for j in range(0, 9):
            matrix_ui[i].append(symbols[0][0])

def display_matrix(): # Displays the 'fake' values
    for i in range(0, 9):
        print(i + 1, end = '')
        for j in range(0, 9): print(matrix_ui[i][j], end = '') # Parsing each line
        print()
    print(' ', end = '')
    for i in range(0, 9): print(i + 1, end = '')
    print()

def update_matrix(i, j): # Input is taken from keyboard & validated in main
    # if player_input == '?': matrix_ui[i][j] = '?'
    # else:
    matrix_ui[i][j] = symbols[matrix[i][j]][-1]
    if matrix[i][j] == 0:
        try:
            if matrix[i + 1][j] == 0 and matrix_ui[i][j] == '\u2588':
                update_matrix(i + 1, j)
        except IndexError: print("Index error circumvented.")
        try:
            if matrix[i][j + 1] == 0 and matrix_ui[i][j] == '\u2588':
                update_matrix(i, j + 1)
        except IndexError: print("Index error circumvented.")
        try:
            if matrix[i - 1][j] == 0 and matrix_ui[i][j] == '\u2588':
                update_matrix(i - 1, j)
        except IndexError: print("Index error circumvented.")
        try:
            if matrix[i][j - 1] == 0 and matrix_ui[i][j] == '\u2588':
                update_matrix(i, j - 1)
        except IndexError: print("Index error circumvented.")

def space_is_available(i, j):
    if matrix_ui[i][j] == '\u2588': return True
    return False

def generate_mines(i, j):
    no = 0
    while no < 9:
        die1 = random.randint(0, 8)
        die2 = random.randint(0, 8)
        if space_is_available(die1, die2) == True and (die1 != i or die2 != j):
            matrix[die1][die2] == -1
            update_matrix(die1, die2)
            no += 1
    generate_numbers()

def generate_numbers(): # Tiles always display the number of mines within a 1 tile radius
    for i in range(0, 9):
        for j in range(0, 9):
            try:
                if matrix[i - 1][j - 1] == -1: matrix[i][j] += 1
            except IndexError: print("Index error circumvented.")
            try:
                if matrix[i - 1][j] == -1: matrix[i][j] += 1
            except IndexError: print("Index error circumvented.")
            try:
                if matrix[i - 1][j + 1] == -1: matrix[i][j] += 1
            except IndexError: print("Index error circumvented.")
            try:
                if matrix[i][j - 1] == -1: matrix[i][j] += 1
            except IndexError: print("Index error circumvented.")
            try:
                if matrix[i][j + 1] == -1: matrix[i][j] += 1
            except IndexError: print("Index error circumvented.")
            try:
                if matrix[i + 1][j - 1] == -1: matrix[i][j] += 1
            except IndexError: print("Index error circumvented.")
            try:
                if matrix[i + 1][j] == -1: matrix[i][j] += 1
            except IndexError: print("Index error circumvented.")
            try:
                if matrix[i + 1][j + 1] == -1: matrix[i][j] += 1
            except IndexError: print("Index error circumvented.")

def reveal_matrix(): # For troubleshooting
    for i in range(0, 9):
        for j in range(0, 9):
            matrix_ui[i][j] = symbols[matrix[i][j]][-1]
    display_matrix()

# def navigate_matrix():

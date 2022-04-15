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
    matrix_ui[i][j] = symbol[matrix[i][j]][-1]
    if matrix[i][j] == 0:
        if matrix[i + 1][j] == 0: update_matrix(i + 1, j)
        if matrix[i][j + 1] == 0: update_matrix(i, j + 1)
        if matrix[i - 1][j] == 0: update_matrix(i - 1, j)
        if matrix[i][j - 1] == 0: update_matrix(i, j - 1)

def space_is_available(i, j):
    if matrix_ui[i][j] == '\u2588': return True
    return False
# def generate_mines(first_placement):
# def navigate_matrix():

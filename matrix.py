matrix = []
symbols = {-1: ('\u2588', '*'), 0: ('\u2588', ''), 1: ('\u2588', '1'), 2: ('\u2588', '2'), 3: ('\u2588', '3'), 4: ('\u2588', '4'), 5: ('\u2588', '5'), 6: ('\u2588', '6'), 7: ('\u2588', '7'), 8: ('\u2588', '8')}  # \u2588 means █, \u1F4A3 means Ὂ in unicode
def generate_matrix():
    for i in range(0, 9):
        matrix.append([])
        for j in range(0, 9):
            matrix[i].append(0)
def display_matrix():
    for i in range(0, 9):
        print(i + 1, end = '')
        for j in range(0, 9): print(matrix[i][j], end = '') # Parsing each line
        print()
    print(' ', end = '')
    for i in range(0, 9): print(i + 1, end = '')
# def generate_mines(first_placement):
# def update_matrix(player_input):
generate_matrix()
display_matrix()

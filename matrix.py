matrix = []
def generate_matrix():
    for i in range(0, 9):
        matrix.append([])
        for j in range(0, 9):
            matrix[i].append('\u2588') # \u2588 means █ in unicode
def display_matrix():
    for i in range(0, 9):
        print(i + 1, end = '')
        for j in range(0, 9): print(matrix[i][j], end = '') # Parsing each line
        print()
    print(' ', end = '')
    for i in range(0, 9): print(i + 1, end = '')
# generate_matrix()
# display_matrix()

import random
matrix = []
matrix_ui = []
counter = 0
symbols = {-1: ('\u2588', '*'), 0: ('\u2588', ' '), 1: ('\u2588', 1), 2: ('\u2588', 2), 3: ('\u2588', 3), 4: ('\u2588', 4), 5: ('\u2588', 5), 6: ('\u2588', 6), 7: ('\u2588', 7), 8: ('\u2588', 8), '?': None}  # \u2588 means █, \u1F4A3 means Ὂ in unicode
def generate_matrix(): # Actual values
    for i in range(0, 9):
        matrix.append([])
        for j in range(0, 9):
            matrix[i].append(0) # Everything is 0

def generate_matrix_interface(): # Displayed values
    for i in range(0, 9):
        matrix_ui.append([])
        for j in range(0, 9):
            matrix_ui[i].append(symbols[0][0]) # Everything is █

def display_matrix(): # Displays the 'fake' values
    for i in range(0, 9):
        print(i + 1, end = '#')
        for j in range(0, 9): print(matrix_ui[i][j], end = '') # Parsing each line
        print()
    print('  ', end = '')
    for i in range(0, 9): print('#', end = '')
    print('\n  ', end = '')
    for i in range(0, 9): print(i + 1, end = '')
    print()

def update_matrix(i, j): # Input is taken from keyboard & validated in main
    global counter
    counter += 1
    print("Counter increased. New counter:", counter)
    matrix_ui[i][j] = symbols[matrix[i][j]][1]
    if matrix[i][j] == 0:
        try: # Down
            if matrix[i + 1][j] == 0 and space_is_available(i + 1, j) == True:
                update_matrix(i + 1, j)
            else:
                matrix_ui[i + 1][j] = symbols[matrix[i + 1][j]][1]
                counter += 1
                print("Counter increased. New counter:", counter)
                if matrix[i + 1][j - 1] != 0 and space_is_available(i + 1, j - 1) and (j - 1 >= 0):
                    # Down Left
                    matrix_ui[i + 1][j - 1] = symbols[matrix[i + 1][j - 1]][1]
                    counter += 1
                    print("Counter increased. New counter:", counter)
                if matrix[i + 1][j + 1] != 0 and space_is_available(i + 1, j + 1):
                    # Down Right
                    matrix_ui[i + 1][j + 1] = symbols[matrix[i + 1][j + 1]][1]
                    counter += 1
                    print("Counter increased. New counter:", counter)
        except IndexError: pass
        try: # Right
            if matrix[i][j + 1] == 0 and space_is_available(i, j + 1) == True:
                update_matrix(i, j + 1)
            else:
                matrix_ui[i][j + 1] = symbols[matrix[i][j + 1]][1]
                counter += 1
                print("Counter increased. New counter:", counter)
                if matrix[i - 1][j + 1] != 0 and space_is_available(i - 1, j + 1) and (i - 1 >= 0):
                    # Up Right
                    matrix_ui[i - 1][j + 1] = symbols[matrix[i - 1][j + 1]][1]
                    counter += 1
                    print("Counter increased. New counter:", counter)
                if matrix[i + 1][j + 1] != 0 and space_is_available(i + 1, j + 1):
                    # Down Right
                    matrix_ui[i + 1][j + 1] = symbols[matrix[i + 1][j + 1]][1]
                    counter += 1
                    print("Counter increased. New counter:", counter)
        except IndexError: pass
        try: # Up
            if matrix[i - 1][j] == 0 and space_is_available(i - 1, j) == True and (i - 1 >= 0):
                update_matrix(i - 1, j)
            elif (i - 1 >= 0):
                matrix_ui[i - 1][j] = symbols[matrix[i - 1][j]][1]
                counter += 1
                print("Counter increased. New counter:", counter)
                if matrix[i - 1][j - 1] != 0 and space_is_available(i - 1, j - 1) and (j - 1 >= 0):
                    # Up Left
                    matrix_ui[i - 1][j - 1] = symbols[matrix[i - 1][j - 1]][1]
                    counter += 1
                    print("Counter increased. New counter:", counter)
                if matrix[i - 1][j + 1] != 0 and space_is_available(i - 1, j + 1):
                    # Up Right
                    matrix_ui[i - 1][j + 1] = symbols[matrix[i - 1][j + 1]][1]
                    counter += 1
                    print("Counter increased. New counter:", counter)
        except IndexError: pass
        try: # Left
            if matrix[i][j - 1] == 0 and space_is_available(i, j - 1) == True and (j - 1 >= 0):
                update_matrix(i, j - 1)
            elif (j - 1 >= 0):
                matrix_ui[i][j - 1] = symbols[matrix[i][j - 1]][1]
                counter += 1
                print("Counter increased. New counter:", counter)
                if matrix[i - 1][j - 1] != 0 and space_is_available(i - 1, j - 1) and (i - 1 >= 0):
                    # Up Left
                    matrix_ui[i - 1][j - 1] = symbols[matrix[i - 1][j - 1]][1]
                    counter += 1
                    print("Counter increased. New counter:", counter)
                if matrix[i + 1][j - 1] != 0 and space_is_available(i + 1, j - 1):
                    # Down Left
                    matrix_ui[i + 1][j - 1] = symbols[matrix[i + 1][j - 1]][1]
                    counter += 1
                    print("Counter increased. New counter:", counter)
        except IndexError: pass

def space_is_available(i, j):
    if matrix_ui[i][j] == '\u2588': return True
    return False

def generate_mines(i, j):
    no = 0
    while no < 10:
        die1 = random.randint(0, 8)
        die2 = random.randint(0, 8)
        if space_is_available(die1, die2) == True and (die1 != i or die2 != j):
            matrix[die1][die2] = -1
            no += 1
    generate_numbers()

def generate_numbers(): # Tiles always display the number of mines within a 1 tile radius
    for i in range(0, 9):
        for j in range(0, 9):
            if matrix[i][j] == -1:
                generate_numbers_helper(i - 1, j - 1) # Up Left
                generate_numbers_helper(i - 1, j)     # Up
                generate_numbers_helper(i - 1, j + 1) # Up Right
                generate_numbers_helper(i, j - 1)     # Left
                generate_numbers_helper(i, j + 1)     # Right
                generate_numbers_helper(i + 1, j - 1) # Down Left
                generate_numbers_helper(i + 1, j)     # Down
                generate_numbers_helper(i + 1, j + 1) # Down Right

def generate_numbers_helper(i, j):
    try:
        if matrix[i][j] != -1 and (i >= 0) and (j >= 0):
            matrix[i][j] += 1
    except IndexError: pass

def reveal_matrix():
    for i in range(0, 9):
        for j in range(0, 9):
            matrix_ui[i][j] = symbols[matrix[i][j]][-1]
    display_matrix()

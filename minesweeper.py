import matrix
print("Welcome to Minesweeper! Uncover all the rectangles while avoiding the mines to win!")
matrix.generate_matrix()
matrix.generate_matrix_interface()
matrix.display_matrix()
while True: # Input
    try:
        player_i = int(input("Awaiting input for horizontal axis(i):")) - 1
        while player_i < 0 or player_i > 8:
            player_i = int(input("Try a number between 1 and 9.\n")) - 1
        player_j = int(input("Awaiting input for vertical axis(j):")) - 1
        while player_j < 0 or player_j > 8:
            player_j = int(input("Try a number between 1 and 9.\n")) - 1
        matrix.generate_mines(player_i, player_j)
        matrix.generate_numbers()
        matrix.update_matrix(player_i, player_j)
        # matrix.display_matrix()
        matrix.reveal_matrix()
        break
    except ValueError:
        print("Try a number.\n")
# matrix.reveal_matrix()
# Game Loop
while True:
    player_i = int(input("Awaiting input for horizontal axis(i):")) - 1
    player_j = int(input("Awaiting input for vertical axis(j):")) - 1
    if player_i in range(0, 9) and player_j in range(0, 9):
        if  matrix.space_is_available(player_i, player_j) == True:
            matrix.update_matrix(player_i, player_j)
    matrix.display_matrix()

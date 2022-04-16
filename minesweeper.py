import matrix
print("Welcome to Minesweeper! Uncover all the rectangles while avoiding the mines to win!")

matrix.generate_matrix()
matrix.generate_matrix_interface()
matrix.display_matrix()

player_i = int(input("Awaiting input for horizontal axis(i):")) - 1
player_j = int(input("Awaiting input for vertical axis(j):")) - 1
if player_i in range(0, 9) and player_j in range(0, 9):
    matrix.generate_mines(player_i, player_j)
    matrix.generate_numbers()
    # matrix.reveal_matrix()
    matrix.update_matrix(player_i, player_j)
matrix.display_matrix()
# matrix.reveal_matrix()
# Game Loop
while True:
    player_i = int(input("Awaiting input for horizontal axis(i):")) - 1
    player_j = int(input("Awaiting input for vertical axis(j):")) - 1
    if player_i in range(0, 9) and player_j in range(0, 9):
        if  matrix.space_is_available(player_i, player_j) == True:
            matrix.update_matrix(player_i, player_j)
    matrix.display_matrix()

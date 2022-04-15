import matrix
print("Welcome to Minesweeper! Uncover all the rectangles while avoiding the mines to win!")

matrix.generate_matrix()
matrix.generate_matrix_interface()
matrix.display_matrix()

# Game Loop
while True:
    player_i = input("Awaiting input for horizontal axis(i):")
    player_j = input("Awaiting input for vertical axis(j):")
    if player_i in range(1, 10) and player_j in range(1, 10):
        if  matrix.space_is_available(player_i, player_j) == True:
            matrix.update_matrix(player_i, player_j)

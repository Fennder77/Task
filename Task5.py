def create_grid(rows, cols):
    grid = [['-' for _ in range(cols)] for _ in range(rows)]
    return grid

def display_grid(grid):
    for row in grid:
        print(' '.join(row))

rows = 3
cols = 3

tic_tac_toe_board = create_grid(rows, cols)

print("Tic-Tac-Toe Board:")
display_grid(tic_tac_toe_board)

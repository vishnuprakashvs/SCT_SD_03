def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def find_empty_location(board):
    # Find the next empty location in the board (marked by 0)
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board, num, pos):
    # Check if the number 'num' is valid to place at position 'pos' (row, col)
    
    # Check row
    for i in range(9):
        if board[pos[0]][i] == num and i != pos[1]:
            return False
    
    # Check column
    for i in range(9):
        if board[i][pos[1]] == num and i != pos[0]:
            return False
    
    # Check 3x3 box
    box_row = pos[0] // 3 * 3
    box_col = pos[1] // 3 * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    
    return True

def solve_sudoku(board):
    # Use recursive backtracking to solve the Sudoku puzzle
    empty = find_empty_location(board)
    if not empty:
        return True  # Board is completely filled
    
    row, col = empty
    
    for num in range(1, 10):  # Numbers 1 to 9
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            
            if solve_sudoku(board):
                return True
            
            board[row][col] = 0  # Backtrack if solution not found
    
    return False

# Example usage:
if __name__ == "__main__":
    # Example Sudoku board (0 represents empty cells)
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    print("Original Sudoku board:")
    print_board(board)
    
    if solve_sudoku(board):
        print("\nSolved Sudoku board:")
        print_board(board)
    else:
        print("No solution exists for the given Sudoku board.")

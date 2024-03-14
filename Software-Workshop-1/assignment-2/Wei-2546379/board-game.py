
def generate_board():
    # TODO: Implement code to generate a 3x3 Sudoku board
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    return board

def print_board(board):
    # TODO: Implement code to print the Sudoku board
    for row in board:
        print(f"{row[0]} | {row[1]} | {row[2]}", end="")
        print("\n---------")
    
def place_number(board, number, row, col):
    # TODO: Implement code to place a number on the board. For example the value (1,0,0) means number is 1, row is 0 and col is 0)
    if board[row][col] == 0:
        board[row][col] = number
    # TODO: check Illegal move e.g. this position is already taken if (1,0,0) is repeated for the next iteration it should display an error that this position is already taken and should return False
    else:
        print(f"Error: the number {number} cannot be placed in position ({row}, {col}) because a number already exists")
        return False
    return True

def check_win(board,current_player):
    # TODO: Implement code to check for a winner based on the sum of rows or columns
    # TODO: check all combinations e.g. horizontally, vertically, diagonally, if any of these equal to 15 its a win
    length = len(board)
    for row in range(length):
        sum_row = 0
        for col in range(length):
            sum_row += board[row][col]
        if sum_row == 15:
            print(f"Player {current_player} wins by  summing to  15 horizontally")
            return True
    
    for row in range(length):
        sum_col = 0
        for col in range(length):
            sum_col += board[col][row]
        if sum_col == 15:
            print(f"Player {current_player} wins by  summing to  15 vertically")
            return True

    sum_dia = sum(board[i][i] for i in range(3))
    if sum_dia == 15:
        print(f"Player {current_player} wins by  summing to  15 diagonally")
        return True
    
    sum_dia = sum(board[i][-i] for i in range(3))
    if sum_dia == 15:
        print(f"Player {current_player} wins by  summing to  15 diagonally")
        return True

    return False

# Example Usage without user input
def play_sudoku():
    current_player = 1
    game_board = generate_board() # your first function call starts from here

# Automated moves
    #some of the automatid moves are as follows, uncomment one by one for checking, you can add your moves as well.
    # moves = [(1, 0, 0), (2, 1, 1), (3, 2, 2), (4, 0, 1), (5, 1, 2), (6, 2, 0), (7, 0, 2), (8, 1, 0), (9, 2, 1)] #1 win vertically
    # moves = [(1, 0, 0), (2, 0, 1), (3, 0, 2), (4, 1, 0), (5, 1, 1), (6, 1, 2), (7, 2, 0), (8, 2, 1), (9, 2, 2)]#2 wins horizontally
    moves = [(5,0,0),(5,0,1),(5,1,1),(5,2,2)]#2 wins diagnally
    # moves = [(2,0,0),(2,0,1),(9,1,0),(9,0,2),(4,2,0)]#1 wins vertically
    # moves = [(2, 0, 0), (2, 0, 1), (9, 1, 0), (9, 0, 2), (3, 2, 0),(5,1,2),(2,2,1),(1,2,2)]# 2 wins vertically
    # moves = [(1, 0, 0), (2, 0, 1), (3, 0, 2), (1, 1, 0), (2, 1, 1), (3, 1, 2), (1, 2, 0), (2, 2, 1), (3, 2, 2)] #no win scenario

    count = 0 # this counter will be used for the case where the board is full (all 9 slots are occupied) and no player has won the game
    print_board(game_board)
    print()
    for move in moves:
        number, row, col = move
        count = count+1
        print(f"It's Player {current_player}'s turn.")
        if 0 <= row < 3 and 0 <= col < 3:
            # TODO: Call the place_number function to place the number on the board
            place_number(game_board, number, row, col)
            print_board(game_board)

            # TODO: Check for a winner using the check_win function
            result = check_win(game_board, current_player)
            if result:
                break

            # TODO: Update the current player for the next turn
            if current_player == 1:
                current_player = 2
            else:
                current_player = 1

        else:
            print("Invalid move. Try again.")
            break  # Stop the game if an invalid move is made when the position is not correct
    if not result:
        print("No win")

if __name__ == "__main__":
    play_sudoku()

"""
import random
"""
import random


def generate_square_board():
    square_board = [[0 for n in range(2)] for n in range(2)]
    """
    change square_board above to reflect the 2 X 2 board
    insert code here to generate a square board of 2 X 2 with zeros
    """
    return square_board

def print_board(square_board):
   """

   :param square_board:
   print the board as instructed
   """
   for row in square_board:
        print("|", end="")
        for element in row:
            print(f" {element:2} |", end="")
        print("\n\n")
    #print(f"| {square_board[0][0]}| {square_board[0][1]} |\n\n| {square_board[1][0]}| {square_board[1][1]} |\n")



def generate_numbers(square_board):
    """
    :param square_board:
    generate the random numbers to replace all zeros on the board
    """
    for i in range(len(square_board)):
        for j in range(len(square_board[i])):
            # Generate a random number (import random) from 1 to
            # 20 to replace each zero on the board
            square_board[i][j] = random.randint(0, 20)
    return square_board


def calculate_win(square_board):
    message = " "
    """
    :param square_board: 
    determine a win
    message = "There is a win"
    message = "No win"
    """
    win_num = list(range(10, 81, 10))
    result = sum(square_board[0]) + sum(square_board[1])
    # print(f"Sum of the square board is: {result}")
    if result in win_num:
        message = "There is a win"
    else:
        message = "No win"
    return (message)

"""
this part of the coding is for testing purposes only
"""
square_board = generate_square_board()
generate_numbers(square_board)
print_board(square_board)
message = calculate_win(square_board)
print(message)

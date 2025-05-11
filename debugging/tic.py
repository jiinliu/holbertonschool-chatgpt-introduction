#!/usr/bin/python3
def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:  # Don't print divider after last row
            print("-" * 9)  # Longer divider to match board width

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        
        # Check for draw condition
        if is_board_full(board) and not check_winner(board):
            print("Game ends in a draw!")
            break
            
        # Get and validate player input
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input! Row and column must be 0, 1, or 2.")
                continue
                
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue
            
        # Place marker if spot is empty
        if board[row][col] == " ":
            board[row][col] = player
            
            # Check for win after move
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break
                
            # Switch player
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

tic_tac_toe()

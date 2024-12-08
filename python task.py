import random

# Function to draw the Tic-Tac-Toe grid
def draw_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check for a winner
def check_winner(board,current_player):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

# Function to check for any available spots 
def available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

# Function for the computer to make a move
def computer_move(board):
    row, col = random.choice(available_moves(board))
    return row, col

# Main function to run the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]  # Initial empty board
    current_player = "X"  # X always starts

    print("Tic-Tac-Toe Game")
    draw_board(board)

    while True:
        if current_player == "X":
            # Player X move (human or AI - you can modify for human input if desired)
            print("Player X's turn")
            row, col = computer_move(board)
        else:
            # Player O move (human or AI - you can modify for human input if desired)
            print("Player O's turn")
            row, col = computer_move(board)

        # Place the move on the board
        board[row][col] = current_player
        draw_board(board)

        # Check for winner
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break

        # Check for a draw (no available moves)
        if not available_moves(board):
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Run the game
play_game()
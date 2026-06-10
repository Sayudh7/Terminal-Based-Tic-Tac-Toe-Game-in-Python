# Terminal-based Tic-Tac-Toe (2 Players)

def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print("\n")


def check_winner(board, player):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    for pattern in win_patterns:
        if all(board[pos] == player for pos in pattern):
            return True
    return False


def board_full(board):
    return all(cell in ["X", "O"] for cell in board)


def tic_tac_toe():
    board = [str(i) for i in range(1, 10)]
    current_player = "X"

    print("=== TIC-TAC-TOE ===")
    print("Choose positions using numbers 1-9.")
    print_board(board)

    while True:
        try:
            move = int(input(f"Player {current_player}, enter position (1-9): "))

            if move < 1 or move > 9:
                print("Please enter a number between 1 and 9.")
                continue

            if board[move - 1] in ["X", "O"]:
                print("That position is already taken.")
                continue

            board[move - 1] = current_player
            print_board(board)

            if check_winner(board, current_player):
                print(f"🎉 Player {current_player} wins!")
                break

            if board_full(board):
                print("It's a draw!")
                break

            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    while True:
        tic_tac_toe()

        again = input("\nPlay again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing!")
            break
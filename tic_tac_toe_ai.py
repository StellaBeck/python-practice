import random

WIN_PATTERNS = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]


def print_board(board):
    view = [cell if cell != " " else str(i + 1) for i, cell in enumerate(board)]
    print()
    print(f" {view[0]} | {view[1]} | {view[2]}")
    print("---+---+---")
    print(f" {view[3]} | {view[4]} | {view[5]}")
    print("---+---+---")
    print(f" {view[6]} | {view[7]} | {view[8]}")
    print()


def winner(board):
    for a, b, c in WIN_PATTERNS:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    if " " not in board:
        return "draw"
    return None


def available_moves(board):
    return [i for i, cell in enumerate(board) if cell == " "]


def human_turn(board):
    while True:
        move = input("Choose position (1-9): ").strip()
        if not move.isdigit():
            print("Enter a number")
            continue
        pos = int(move) - 1
        if pos not in range(9):
            print("Out of range")
            continue
        if board[pos] != " ":
            print("Spot already taken")
            continue
        board[pos] = "X"
        break


def find_winning_move(board, mark):
    for move in available_moves(board):
        test_board = board.copy()
        test_board[move] = mark
        if winner(test_board) == mark:
            return move
    return None


def computer_turn(board):
    move = find_winning_move(board, "O")
    if move is None:
        move = find_winning_move(board, "X")
    if move is None and 4 in available_moves(board):
        move = 4
    if move is None:
        corners = [i for i in [0, 2, 6, 8] if i in available_moves(board)]
        if corners:
            move = random.choice(corners)
    if move is None:
        move = random.choice(available_moves(board))
    board[move] = "O"
    print(f"Computer chose position {move + 1}")


def play_game():
    board = [" "] * 9
    print("You are X. Computer is O.")
    print_board(board)

    while True:
        human_turn(board)
        print_board(board)
        state = winner(board)
        if state:
            return state

        computer_turn(board)
        print_board(board)
        state = winner(board)
        if state:
            return state


def main():
    player_wins = 0
    computer_wins = 0
    draws = 0

    while True:
        result = play_game()
        if result == "X":
            player_wins += 1
            print("You win")
        elif result == "O":
            computer_wins += 1
            print("Computer wins")
        else:
            draws += 1
            print("Draw")

        print(f"Score -> You: {player_wins}, Computer: {computer_wins}, Draws: {draws}")
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            break


if __name__ == "__main__":
    main()

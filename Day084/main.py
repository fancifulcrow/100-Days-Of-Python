# board is an array of 3 arrays each with 3 items
board = [[" " for _ in range(3)] for _ in range(3)]


# print the board
def print_board():
    for row in board:
        print(" | ".join(row))
        print("---------")


def check_winner(player):
    # horizontal win
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # vertical win
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # diagonal win
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Check if the board is full
def board_is_full():
    return all(cell != ' ' for row in board for cell in row)


current_player = 'X'

while True:
    print_board()

    play = input(f"Player {current_player}, enter row and column (e.g., 1 2): ")

    try:
        row = int(play.split(" ")[0]) 
        col = int(play.split(" ")[1])
    except (TypeError, ValueError):
        print("Please input the correct syntax i.e. 1 2")
        continue
    else:
        if row > 3 or row < 1 or col > 3 or col < 1:
            print("The position given is off the board. Try again")
            continue

    # check if the position is empty  
    if board[row - 1][col - 1] == ' ':
        board[row - 1][col - 1] = current_player

        # end of game conditions
        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        elif board_is_full():
            print_board()
            print("It's a tie!")
            break

        # change to next player
        current_player = 'X' if current_player == 'O' else 'O'
    else:
        print("That cell is already taken. Try again.")

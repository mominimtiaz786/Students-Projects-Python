def draw_board(board):
    # This function prints the Tic Tac Toe board.
    # The board is represented as a list of strings, where each string is a row on the board.
    # The board is 3x3, so the list has 3 elements.
    # Each element is a string with 3 characters: 'X', 'O', or ' '.
    # The characters represent the cells on the board, with 'X' and 'O' being the players' pieces
    # and ' ' being an empty cell.
    print(f' {board[0][0]} | {board[0][1]} | {board[0][2]} ')
    print('-----------')
    print(f' {board[1][0]} | {board[1][1]} | {board[1][2]} ')
    print('-----------')
    print(f' {board[2][0]} | {board[2][1]} | {board[2][2]} ')

def get_move(player, board):
    # This function gets the next move from the player.
    # It prompts the player to enter the row and column where they want to place their piece.
    # The function checks that the input is valid (i.e., a valid row and column on the board)
    # and that the cell is empty.
    # If the input is invalid, the function prints an error message and prompts the player again.
    while True:
        row = int(input(f'{player}, enter the row (1-3): ')) - 1
        col = int(input(f'{player}, enter the column (1-3): ')) - 1
        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
            board[row][col] = player
            break
        print('Invalid move, try again.')

def has_won(player, board):
    # This function checks if the player has won the game.
    # It checks all rows, columns, and diagonals on the board to see if they are all occupied by the player's piece.
    # If any of them are, it returns True. Otherwise, it returns False.
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def main():
    # This is the main function of the game.
    # It initializes the board as an empty 3x3 grid and the players as 'X' and 'O'.
    # It then enters a loop that continues until the game is over (either someone has won or there are no more empty cells).
    # In the loop, it calls the draw_board() function to draw the current state of the board,
    # and then calls the get_move() function for the current player to get their next move and update the board.
    # It then checks if the current player has won the game by calling the has_won() function.
    # If they have, it prints a message announcing the winner and breaks out of the loop.
    # If no one has won and there are still empty cells on the board, it switches to the other player and goes back to the beginning of the loop.
    # If no one has won and there are no more empty cells, it prints a message announcing a tie.
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0
    while True:
        draw_board(board)
        row, col = get_move(players[current_player], board)
        board[row][col] = players[current_player]
        if has_won(board, players[current_player]):
            print(f'{players[current_player]} has won!')
            break
        if all(all(cell != ' ' for cell in row) for row in board):
            print('The game is a tie!')
            break
        current_player = (current_player + 1) % 2


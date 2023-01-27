import random


def display_board(board):
    print(f'{board[1]:^4}|  {board[2]:^2}|  {board[3]:^2}')
    print('-' * 3, '+', '-' * 2, '+', '-' * 4)
    print(f'{board[4]:^4}|  {board[5]:^2}|  {board[6]:^2}')
    # print('-' * 15)
    print('-' * 3, '+', '-' * 2, '+', '-' * 4)
    print(f'{board[7]:^4}|  {board[8]:^2}|  {board[9]:^2}')


def player_pick():
    marker = ' '
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player1: Do you want to be X or O: ").upper()
        player1 = marker
        if player1 == "X":
            player2 = "O"
        else:
            player2 = 'X'
        return player1, player2


def check_winner(board, player):
    win_positions = [[1, 2, 3], [1, 4, 7], [1, 5, 9], [4, 5, 6], [7, 8, 9], [2, 5, 8], [3, 6, 9], [3, 5, 7]]
    for pos in win_positions:
        if board[pos[0]] == player and board[pos[1]] == player and board[pos[2]] == player:
            return True
    return False


def check_board_full(board):
    if ' ' in board[1:]:
        return True
    return False


def player_order(player1, player2):
    choice = random.randint(0, 10)
    if choice % 2 == 0:
        return player1
    return player2


def play_game():
    board = [" "] * 10
    player1, player2 = player_pick()
    act_player = player_order(player1, player2)
    game_on = True
    while game_on:
        print(display_board(board))
        place = int(input(f"Player {act_player}, choose where to put your marker: "))
        if board[place] == ' ':
            board[place] = act_player
        else:
            print("There is a marker there already, please select a new position")
        if check_winner(board, act_player):
            print(display_board(board))
            print(f"{act_player} is the winner!")
            game_on = False
        if not check_board_full(board):
            print("There is a tie, no winners")
            game_on = False
        if act_player == "X":
            act_player = "O"
        else:
            act_player = "X"


play_game()
play_again = input("Would you like to play again, Y or N: ").upper()
if play_again == "Y":
    play_game()
else:
    print("Thank you for playing!")

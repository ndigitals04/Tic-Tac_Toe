tic_tac_toe_board= {"top-l":" ", "top-m":" ", "top-r":" ",
"mid-l":" ", "mid-m": " ", "mid-r": " ", 
"low-l": " ","low-m":" ", "low-r":" "}

def printBoard(board):
    print(board["top-l"] + " | " + board["top-m"] + " | " + board["top-r"])
    print(" --++-- ")
    print(board["mid-l"] + " | " + board["mid-m"] + " | " + board["mid-r"])
    print(" --++-- ")
    print(board["low-l"] + " | " + board["low-m"] + " | " + board["low-r"])

# printBoard(tic_tac_toe_board)
def playTicTacToe(board,display_board_func, check_winner_func):
    turn = "X"
    for i in range(9):
        display_board_func(board)
        print("it's " + turn + " turn. Input the space you'd like to play")
        move = input()
        while move not in board.keys():
            print("input proper denotation for space you want to play")
            move = input()
        
        while board[move] != " ":
            print(board[move] + " has already played in that space, choose another")
            move= input()
            while move not in board.keys():
                print("input proper denotation for space you want to play")
                move = input()

        board[move] = turn
        winner = check_winner_func(board)
        if winner != None and winner != " " and winner!= "No winner":
            print(f"{winner} is the winner")
            break
        elif winner == "No winner":
            print("No winner for this round")
        # print(result, "xxx")
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
    display_board_func(board)        

def checkForTicTacToeWinner(board):
    if board["top-l"] == board["top-m"] and board["top-m"] == board["top-r"]:
        return board["top-l"]
    elif board["mid-l"] == board["mid-m"] and board["mid-m"] == board["mid-r"] and board["mid-r"]!= " ":
        return board["top-m"]
    elif board["low-l"] == board["low-m"] and board["low-m"] == board["low-r"]:
        return board["low-l"]
    elif board["top-l"] == board["mid-m"] and board["mid-m"] == board["low-r"]:
        return board["top-l"]
    elif board["top-r"] == board["mid-m"] and board["mid-m"] == board["low-l"]:
        return board["top-r"]
    elif board["top-l"] == board["mid-l"] and board["mid-l"] == board["low-l"]:
        return board["top-l"]
    elif board["top-m"] == board["mid-m"] and board["mid-m"] == board["low-m"]:
        return board["top-m"]
    elif board["top-r"] == board["mid-r"] and board["mid-r"] == board["low-r"]:
        return board["top-r"]
    else:
        return "No winner"

playTicTacToe(tic_tac_toe_board,printBoard, checkForTicTacToeWinner)
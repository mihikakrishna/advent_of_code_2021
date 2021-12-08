def removeNum(num,board):
        for row in board:
            for i,val in enumerate(row):
                if val == num: row[i] = 'X'

def endGame(board):
    for row in board:
        if row.count('X') == 5 : 
            return True
    for col in range(5):
        str = ""
        for row in board:
            str += row[col]
        if str.count('X') == 5 : return True
    return False
        

def readInput():
    f = open("day4/4.txt", "r")
    moves = [str(x) for x in f.readline().split(",")]
    boards = []
    while(f.readline()):
            board = []
            for i in range(5):
                board.append(f.readline().split())
            boards.append(board)
    return moves, boards

    
def bingo():
    moves, boards = readInput()
    # print(moves)
    for move in moves:
        for board in boards:
            removeNum(move,board)
            if endGame(board) : return(board,move) 
        
        # for board in boards:
        #     for line in board:
        #         print(line)
        #     print("-----")
        # print("-----------------------------")

def printRes():
    board,move = bingo()
    sum = 0
    for row in board:
        for col in row: 
            if col != 'X': sum += int(col)
    print(sum * int(move))

printRes()

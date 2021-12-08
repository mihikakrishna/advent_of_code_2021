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
    wins = set()
    lastWin = (0,0,0)
    # print(moves)
    for move in moves:
        for i,board in enumerate(boards):
            removeNum(move,board)
            if endGame(board) and i not in wins:
                wins.add(i)
                lastWin = (i+1,board,move) 
            if len(wins) == len(boards): return lastWin
        
        # for board in boards:
        #     for line in board:
        #         print(line)
        #     print("-----")
        # print("-----------------------------")
    return lastWin

def printRes():
    i,board,move = bingo()
    print(i)
    print(move)
    for line in board:
        print(line)
    sum = 0
    for row in board:
        for col in row: 
            if col != 'X': sum += int(col)
    print(sum * int(move))

printRes()

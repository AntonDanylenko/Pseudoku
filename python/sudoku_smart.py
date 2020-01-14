#! /usr/bin/python3

import sys
import copy
import time

AllVals = set([1,2,3,4,5,6,7,8,9])
Cliques=[{0,1,2,3,4,5,6,7,8},\
{9,10,11,12,13,14,15,16,17},\
{18,19,20,21,22,23,24,25,26},\
{27,28,29,30,31,32,33,34,35},\
{36,37,38,39,40,41,42,43,44},\
{45,46,47,48,49,50,51,52,53},\
{54,55,56,57,58,59,60,61,62},\
{63,64,65,66,67,68,69,70,71},\
{72,73,74,75,76,77,78,79,80},\
{0,9,18,27,36,45,54,63,72},\
{1,10,19,28,37,46,55,64,73},\
{2,11,20,29,38,47,56,65,74},\
{3,12,21,30,39,48,57,66,75},\
{4,13,22,31,40,49,58,67,76},\
{5,14,23,32,41,50,59,68,77},\
{6,15,24,33,42,51,60,69,78},\
{7,16,25,34,43,52,61,70,79},\
{8,17,26,35,44,53,62,71,80},\
{0,1,2,9,10,11,18,19,20},\
{3,4,5,12,13,14,21,22,23},\
{6,7,8,15,16,17,24,25,26},\
{27,28,29,36,37,38,45,46,47},\
{30,31,32,39,40,41,48,49,50},\
{33,34,35,42,43,44,51,52,53},\
{54,55,56,63,64,65,72,73,74},\
{57,58,59,66,67,68,75,76,77},\
{60,61,62,69,70,71,78,79,80}\
]
squares = [\
[0,1,2,9,10,11,18,19,20],\
[3,4,5,12,13,14,21,22,23],\
[6,7,8,15,16,17,24,25,26],\
[27,28,29,36,37,38,45,46,47],\
[30,31,32,39,40,41,48,49,50],\
[33,34,35,42,43,44,51,52,53],\
[54,55,56,63,64,65,72,73,74],\
[57,58,59,66,67,68,75,76,77],\
[60,61,62,69,70,71,78,79,80]\
]
rows = [\
[0,1,2,3,4,5,6,7,8],\
[9,10,11,12,13,14,15,16,17],\
[18,19,20,21,22,23,24,25,26],\
[27,28,29,30,31,32,33,34,35],\
[36,37,38,39,40,41,42,43,44],\
[45,46,47,48,49,50,51,52,53],\
[54,55,56,57,58,59,60,61,62],\
[63,64,65,66,67,68,69,70,71],\
[72,73,74,75,76,77,78,79,80],\
]
cols = [\
[0,9,18,27,36,45,54,63,72],\
[1,10,19,28,37,46,55,64,73],\
[2,11,20,29,38,47,56,65,74],\
[3,12,21,30,39,48,57,66,75],\
[4,13,22,31,40,49,58,67,76],\
[5,14,23,32,41,50,59,68,77],\
[6,15,24,33,42,51,60,69,78],\
[7,16,25,34,43,52,61,70,79],\
[8,17,26,35,44,53,62,71,80],\
]
clique_list = [squares, rows, cols]
neighbors = {}

class MyStack:
    def __init__(self, cells = [], list = []):
        self.cells = cells
        self.stack = list

    def __str__(self):
        return str(self.stack)

    def push(self, args):
        self.cells.append(args[0])
        #print(self.cells)
        self.stack.append(args[1])

    def pop(self):
        #print("cells: " + str(self.cells))
        return [self.cells.pop(len(self.cells)-1), self.stack.pop(len(self.stack)-1)]

# class Sudoku:
#     def __init__(self, fileName, boardName):
#         self.boards = Stack()
#         f = open(fileName, "r")
#         df = f.read()
#         lines = df.split('\n')
#         f.close()

def getBoard(argv):
    #print(argv[3])
    name = argv[3]
    f = open(argv[1], "r")
    df = f.read()
    lines = df.split('\n')
    f.close()
    board = []
    temp = ""
    for x in range(len(lines)):
        if name in lines[x]:
            name = lines[x]
            for y in range(x+1, x+10):
                temp+=lines[y]
            temp = temp.replace(',', '')
            board = list(temp)
    return [name, board]

def makeNeighbors():
    for cell in range(81):
        temp = []
        for clique in Cliques:
            if cell in clique:
                for x in clique:
                    if x not in temp:
                        temp.append(x)
        neighbors[cell] = temp
    print(neighbors)

def findClique(cell, search_type):
    if cell==-1:
        #print(search_type)
        return clique_list[search_type][0]
    for clique in clique_list[search_type]:
        if cell in clique:
            return clique
    return None

def nextClique(clique, search_type):
    index = clique_list[search_type].index(clique)
    if not index==8:
        return clique_list[search_type][index+1]
    return None

# def nextOpenCell(board, prev_cell, search_type):
#     clique, start_index = findCliqueAndStartIndex(prev_cell, search_type)
#     next_cell = nextOpenCellinClique(board, clique, start_index)
#     while next_cell==None and not clique_list[search_type].index(clique)==9:
#         clique = clique_list[search_type][clique_list[search_type].index(clique)+1] #makes clique next clique
#         start_index = 0
#         next_cell = nextOpenCellinClique(board, clique, start_index)
#     return next_cell

# def minCell(guess_board):
#     min_index = 0
#     min=10
#     #print("guess_board: ", guess_board)
#     # print("len(guess_board): ", len(guess_board))
#     for x in range(len(guess_board)):
#         if guess_board[x]<min:
#             min = guess_board[x]
#             min_index = x
#     # print("min_index: ", min_index)
#     # print("min: ", min)
#     if min<10:
#         return min_index
#     return 81

def nextOpenCell(board, prev_cell):
    for x in range(prev_cell+1, len(board)):
        if board[x]=='_':
            return x
    return 81

def nextOpenCellinClique(board, prev_cell, clique):
    # if cur_num==4:
    #     print("nextOpenCellinClique")
    #     print("prev_cell, clique: ", prev_cell, clique)
    start_index = 0
    if prev_cell in clique:
        start_index = clique.index(prev_cell)+1
    #print("start_index: ", start_index)
    for x in clique[start_index:]:
        if board[x]=='_':
            # print("prev_cell: ", prev_cell)
            # print("clique: ", clique)
            # if cur_num==4:
            #     print("returns: ", clique[x])
            #     print("-----------------------")
            return x
    return None #if there are no open cells in the clique, main func should handle moving on to next clique

def canPlace(board, cell, num):
    # for clique in Cliques:
    #     if cell in clique:
    #         for place in clique:
    #             if str(board[place])==str(num):
    #                 return False
    # return True
    # print("cell: ", cell)
    # print("neighbors[cell]: ", neighbors[cell])
    for x in neighbors[cell]:
        if str(board[x])==str(num):
            return False
    return True

def isForced(board,cell):
    forced = None
    for num in range(1,10):
        if canPlace(board,cell,num):
            if forced==None:
                forced = num
            else:
                return None
    return forced

def nextForced(board,prev_cell):
    for x in range(prev_cell+1, len(board)):
        if board[x]=='_':
            num = isForced(board,x)
            if not num==None:
                return [x,num]
    return [81,None]

# def numGuesses(board,cell):
#     num_guesses = 0
#     for num in range(0,10):
#         #print("Cell: ", cell)
#         if canPlace(board,cell,num):
#             num_guesses+=1
#     return num_guesses

# def makeGuessBoard(board):
#     guess_board = []
#     for cell in range(len(board)):
#         if board[cell]=='_':
#             guess_board.append(numGuesses(board,cell))
#         else:
#             guess_board.append(10)
#     # print("GUess_board: ", guess_board)
#     # print("LEn(guess_board): ", len(guess_board))
#     return guess_board

def nextValidGuess(board,cell,num):
    temp = [None, False]
    for guess in range(num, 10):
        #print(guess)
        #print("Cell: ", cell)
        if canPlace(board,cell,guess):
            if temp[0]==None:
                temp = [guess, True]
            else:
                return [temp[0], False]
    return temp

def printBoard(board):
    result = ""
    for x in range(9):
        for y in range(8):
            result += str(board[x*9+y]) + ","
        result += str(board[x*9+8]) + "\n"
    print(result)

def writeBoard(argv,name,board):
    f = open(argv[2], "w")
    #f.write(name.replace("unsolved", "solved") + "\n")
    for x in range(9):
        for y in range(8):
            f.write(str(board[x*9+y]) + ",")
        f.write(str(board[x*9+8]) + "\n")
    f.close()

# States
NEW_CELL = 0
FIND_NEXT_CELL = 1
BACKTRACK = 2
TEST_CLIQUE = 3
NEXT_CLIQUE = 4
NEXT_SEARCH_TYPE = 5
NEXT_NUM = 6
REPEAT = 7
NAIVE_TIME = 8
START_STRAT = 9
FIND_NEXT_FORCED = 10

def execute(board):
    start_time = time.time()
    makeNeighbors()
    search_type = 0
    clique = findClique(-1,search_type)
    cell = nextOpenCellinClique(board,-1,clique) #makes cell first open cell in first square
    cur_num = 1
    state = TEST_CLIQUE
    temp_cell = None
    num_placed = 0
    mystack = MyStack()
    nback = 0
    guess_board = []
    while True:
        if state == START_STRAT:
            search_type = 0
            clique = findClique(-1,search_type)
            cell = nextOpenCellinClique(board,-1,clique) #makes cell first open cell in first square
            cur_num = 1
            state = TEST_CLIQUE
            temp_cell = None
            num_placed = 0
            continue

        if state == TEST_CLIQUE:
            #print("state: TEST_CLIQUE")
            # print("Search_type: ", search_type)
            # print("Clique: ", clique)
            #print("Cell: ", cell)
            if not cell==None and canPlace(board, cell, cur_num):
                # if cur_num==4:
                #     print("canPlace on cell: ", cell)
                if temp_cell==None:
                    # if cur_num==4:
                    #     print("temp_cell, cell: ", temp_cell, cell)
                    temp_cell = cell
                else:
                    # if cur_num==4:
                    #     print("move on to NEXT_CLIQUE")
                    state = NEXT_CLIQUE
                    continue
            cell = nextOpenCellinClique(board,cell,clique)
            #print("Cell: ", cell)
            if cell==None:
                # if cur_num==4:
                #     print("--------------------------------------")
                #     print("END OF CLIQUE")
                #     print("CUR_NUM 4")
                #     print("clique: ", clique)
                #     print("search_type: ", search_type)
                #     print("temp_cell: ", temp_cell)
                #     print("--------------------------------------")
                if not temp_cell==None:
                    #printBoard(board)
                    board[temp_cell] = cur_num
                    num_placed+=1
                state = NEXT_CLIQUE
            continue

        if state == NEXT_CLIQUE:
            clique = nextClique(clique,search_type)
            temp_cell = None
            if clique==None:
                state = NEXT_SEARCH_TYPE
                continue
            cell = nextOpenCellinClique(board,-1,clique)
            # if cur_num==4:
            #     print("////////////////////")
            #     print("state: NEXT_CLIQUE")
            #     print("clique: ", clique)
            #     print("cell: ", cell)
            #     print("////////////////////")
            state = TEST_CLIQUE
            continue

        if state == NEXT_SEARCH_TYPE:
            #print("state: NEXT_SEARCH_TYPE")
            search_type+=1
            if search_type==3:
                state = NEXT_NUM
                continue
            clique = findClique(-1,search_type)
            cell = nextOpenCellinClique(board,-1,clique)
            state = TEST_CLIQUE
            continue

        if state == NEXT_NUM:
            #print("state: NEXT_NUM")
            cur_num+=1
            if cur_num==10:
                state = REPEAT
                continue
            search_type=0
            clique = findClique(-1,search_type)
            cell = nextOpenCellinClique(board,-1,clique)
            state = TEST_CLIQUE
            #print("move back to TEST_CLIQUE")
            continue

        if state == REPEAT:
            #printBoard(board)
            if num_placed==0:
                state = NAIVE_TIME
                continue
            search_type = 0
            clique = findClique(-1,search_type)
            cell = nextOpenCellinClique(board,-1,clique) #makes cell first open cell in first square
            cur_num = 1
            temp_cell = None
            num_placed = 0
            state = TEST_CLIQUE
            continue

        if state == NAIVE_TIME:
            #print("Smart strat time: " + str(time.time()-start_time))
            #printBoard(board)
            #guess_board = makeGuessBoard(board)
            #print(guess_board)
            # print("GUEss_board: ", guess_board)
            # print("LEN(guess_board): ", len(guess_board))
            cell = nextOpenCell(board,-1)
            state = NEW_CELL
            if cell == 81:
                break
            continue

        # we're on a new open cell
        if state == NEW_CELL:
            #printBoard(board)
            #print("-------")
            guess,forced = nextValidGuess(board,cell,1)
            #print ("NEW_CELL,cell,guess,forced",cell,guess,forced)
            if not guess:
                # failed to find a valid guess for this cell, backtrack
                state = BACKTRACK
            else:
                #print("cell: ", cell)
                board[cell] = guess
                #guess_board = makeGuessBoard(board)
                #print(cell)
                if not forced:
                    mystack.push([cell,board[:]])
                    state = START_STRAT
                    continue
                state = FIND_NEXT_FORCED
            continue

        # find a new open cell
        if state == FIND_NEXT_CELL:
            cell = nextOpenCell(board,cell)
            if cell == 81:
                # Solution!
                break
            state = NEW_CELL
            continue

        if state == FIND_NEXT_FORCED:
            temp = None
            cell, temp = nextForced(board,cell)
            if cell == 81:
                cell = nextOpenCell(board,-1)
                if cell == 81:
                    break
                state = NEW_CELL
                continue
            board[cell] = temp
            continue

        # backtrack
        if state == BACKTRACK:
            nback += 1
            #print("cell: " + str(cell))
            cell,board = mystack.pop()
            old_guess = board[cell]
            guess,forced = nextValidGuess(board,cell,old_guess+1)  # note: state cannot be forced
            #print('BACKTRACK,cell,guess,forced',cell,guess,forced)
            if not guess:
                state = BACKTRACK
            else:
                board[cell] = guess
                #guess_board = makeGuessBoard(board)
                if not forced:
                    mystack.push([cell,board[:]])
                    state = START_STRAT
                    continue
                state = FIND_NEXT_CELL
            continue

    time_elapsed = time.time() - start_time
    # print("Solution time: " + str(round(time_elapsed, 3)))
    # print ('Solution!, with backtracks: ',nback)
    # printBoard(board)
    return board

# print(execute(['_', '_', '_', '_', '_', '_', '_', '_', '_',\
#                 '_', '7', '9', '_', '5', '_', '1', '8', '_',\
#                 '8', '_', '_', '_', '_', '_', '_', '_', '7',\
#                 '_', '_', '7', '3', '_', '6', '8', '_', '_',\
#                 '4', '5', '_', '7', '_', '8', '_', '9', '6',\
#                 '_', '_', '3', '5', '_', '2', '7', '_', '_',\
#                 '7', '_', '_', '_', '_', '_', '_', '_', '5',\
#                 '_', '1', '6', '_', '3', '_', '4', '2', '_',\
#                 '_', '_', '_', '_', '_', '_', '_', '_', '_']))

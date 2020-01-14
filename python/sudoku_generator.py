#! /usr/bin/python3

from python import sudoku_smart
import random
import os

class MyStack2:
    def __init__(self, cells = [], list = [], available = []):
        self.cells = cells
        self.stack = list
        self.available = available

    def __str__(self):
        return str(self.stack)

    def push(self, args):
        self.cells.append(args[0])
        #print(self.cells)
        self.stack.append(args[1])
        self.available.append(args[2])

    def pop(self):
        #print("cells: " + str(self.cells))
        return [self.cells.pop(len(self.cells)-1), self.stack.pop(len(self.stack)-1), self.available.pop(len(self.available)-1)]

def checkBoard(board):
    for cell_index in range(len(board)):
        num = board[cell_index]
        board[cell_index] = '_'
        if not sudoku_smart.canPlace(board,cell_index,num):
            return False
    return True

def compBoards(b0,b1):
    for index in range(81):
        if b0[index]!=b1[index]:
            return False
    return True

def generateFilled():
    board = ['_' for x in range(81)]
    sudoku_smart.makeNeighbors()
    mystackcells = MyStack2()
    row = 0
    nums_list = [1,2,3,4,5,6,7,8,9]
    while row < 9:
        col = 0
        while col < 9:
            cell_index = col+row*9
            while str(board[cell_index]) == '_':
                if len(nums_list)==0:
                        cell_index, board, nums_list = mystackcells.pop()
                        board[cell_index] = '_'
                        col-=1
                else:
                    num = nums_list[random.randint(0,len(nums_list)-1)]
                    nums_list.remove(num)
                    if sudoku_smart.canPlace(board, cell_index, num):
                        board[cell_index] = num
                        mystackcells.push([cell_index,board[:],nums_list])
                        nums_list = [1,2,3,4,5,6,7,8,9]
                # os.system('cls' if os.name == 'nt' else 'clear')
                # printBoard(board)
                # time.sleep(.5)
            col+=1
        row+=1
    # sudoku_smart.printBoard(board)
    return board

def generatePuzzle(filledNum):
    start_time = sudoku_smart.time.time()
    board = generateFilled()
    puzzle = board[:]
    tried_cell_list = []
    stack = MyStack2()
    while puzzle.count('_')+filledNum<81:
        if len(tried_cell_list)+filledNum>81:
            cell_index, puzzle, tried_cell_list = stack.pop()
        cell_index = random.randint(0,80)
        if not cell_index in tried_cell_list:
            num = puzzle[cell_index]
            puzzle[cell_index] = '_'
            tried_cell_list.append(cell_index)
            if compBoards(sudoku_smart.execute(puzzle[:]),board[:]):
                stack.push([cell_index,puzzle,tried_cell_list])
            else:
                puzzle[cell_index] = num
    # time_elapsed = sudoku_smart.time.time() - start_time
    # print("Generation time: " + str(round(time_elapsed, 3)))
    # writeTime('output.txt',filledNum,round(time_elapsed,3))
    # sudoku_smart.printBoard(puzzle)
    # print(puzzle)
    return puzzle

def writeTime(filename,filledNum,time):
    f = open(filename, "a")
    f.write(str(filledNum) + ": " + str(time) + "\n")
    f.close()

def findAvgTime(filename,filledNum):
    f = open(filename,"r")
    df = f.read()
    lines = df.split('\n')
    f.close()
    sum = 0
    count = 0
    for line in lines:
        if line[0:2]==str(filledNum):
            sum+=float(line[4:])
            count+=1
    return round(sum/count,3)

def strBoard(board):
    ans = ""
    for x in board:
        ans=ans+str(x)+','
    return ans[:-1]

# filled = generateFilled()
# print(checkBoard(filled))
# for x in range(5):
#     puzzle = generatePuzzle(24)
# print(findAvgTime('output.txt',24))
# sudoku_smart.printBoard(sudoku_smart.execute(puzzle))

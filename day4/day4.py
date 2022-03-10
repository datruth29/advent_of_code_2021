import pprint
import os

DATADIR = os.path.dirname(os.path.realpath(__file__))
DATAFILE = os.path.join(DATADIR, 'input.txt')

def one_star_solution(data):
    return NotImplemented

def two_star_solution(data):
    return NotImplemented

def get_board(num, boards):
    value = num * 25
    return boards[value:value+25]

def bingo_checker(marked_board):
    if all(marked_board[0:5]):
        return True
    if all(marked_board[5:10]):
        return True
    if all(marked_board[10:15]):
        return True
    if all(marked_board[15:20]):
        return True
    if all(marked_board[20:25]):
        return True
    if all(marked_board[0:25:5]):
        return True
    if all(marked_board[1:25:5]):
        return True
    if all(marked_board[2:25:5]):
        return True
    if all(marked_board[3:25:5]):
        return True
    if all(marked_board[4:25:5]):
        return True
    if all(marked_board[0:25:6]):
        return True
    return False

def play_round(round, marked_boards):
    round_results = [position < round for position in marked_boards]

    for board in range(0, len(marked_boards)/25):
        isBingo = bingo_checker(round_results[board:board+25])
        if isBingo:
            result = (round, get_board(board))

def fmtcols(mylist, cols):
    for i in range(0, len(mylist), cols):
        print(mylist[i:i+cols])
    return None

if __name__ == '__main__':
    with open(DATAFILE) as f:
        draws = list(map(int, f.readline().strip().split(',')))
        boards = []
        for line in f:
            if line.strip() == '':
                continue
            boards.extend(list(map(int, line.strip().split())))

    marked = [0] * len(boards)

    for round, draw in enumerate(draws):
        for index, value in enumerate(boards):
            if value == draw:
                marked[index] = round+1

    board_number = 0
    for value in range(0, 2500, 25):
        board_number += 1
        board = boards[value:value+25]
        mark = marked[value:value+25]
        # print(board_number)
   # print(get_board(0, marked))
   # print(get_board(0, boards))

   # print(len(boards))

    #for round in range(0, len(marked)):
        #print(round)

    

        
    #print(result)
    #fmtcols(isBingo, 5)
    #fmtcols(board, 5)



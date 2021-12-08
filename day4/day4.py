import pprint
import os

PP = pprint.PrettyPrinter(indent=1)
DATADIR = os.path.dirname(os.path.realpath(__file__))
DATAFILE = os.path.join(DATADIR, 'input.txt')

def one_star_solution(data):
    return NotImplemented

def two_star_solution(data):
    return NotImplemented

def get_board(boards):
    

if __name__ == '__main__':
    with open(DATAFILE) as f:
        draws = list(map(int, f.readline().strip().split(',')))
        boards = []
        for line in f:
            if line.strip() == '':
                continue
            boards.extend(list(map(int, line.strip().split())))
    marked = [0] * len(boards)

    for position, draw in enumerate(draws):
        for index, value in enumerate(boards):
            if value == draw:
                marked[index] = position+1
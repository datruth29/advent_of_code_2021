import os

DATADIR = os.path.dirname(os.path.realpath(__file__))
DATAFILE = os.path.join(DATADIR, 'input.txt')

def one_star_solution(data):
    horizontal = 0
    depth = 0
    for line in data:
        command = int(line.strip()[-1::])
        if line[0] == 'f':
            horizontal += command
        if line[0] == 'd':
            depth += command
        if line[0] == 'u':
            depth -= command
    result = horizontal * depth
    return result

def two_star_solution(data):
    horizontal = 0
    depth = 0
    aim = 0
    for line in data:
        command = int(line.strip()[-1::])
        if line[0] == 'f':
            horizontal += command
            depth += aim * command
        if line[0] == 'd':
            aim += command
        if line[0] == 'u':
            aim -= command
    result = horizontal * depth
    return result

if __name__ == "__main__":
    with open(DATAFILE) as f:
        data = f.readlines()

    print("One Star Solution: {}".format(one_star_solution(data)))
    print("Two Star Solution: {}".format(two_star_solution(data)))
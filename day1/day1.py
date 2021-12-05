import os

DATADIR = os.path.dirname(os.path.realpath(__file__))
DATAFILE = os.path.join(DATADIR, 'input.txt')

def one_star_solution(data):
    zipped_list = zip(data, data[1:])
    result = [x[0] < x[1] for x in zipped_list]

    return sum(result)

def two_star_solution(data):
    zipped_list = zip(data, data[1:], data[2:])
    summed_list = list((map(sum, zipped_list)))
    result = one_star_solution(summed_list)

    return result


if __name__ == "__main__":
    data = []
    with open(DATAFILE) as f:
        for line in f:
            data.append(int(line.strip()))
    

    print("One Star Solution: {}".format(one_star_solution(data)))
    print("Twp Star Solution: {}".format(two_star_solution(data)))

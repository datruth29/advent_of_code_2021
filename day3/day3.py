import os

DATADIR = os.path.dirname(os.path.realpath(__file__))
DATAFILE = os.path.join(DATADIR, 'input.txt')

def convert_to_int(str_bin):
    return int("".join(str(x) for x in str_bin), 2)

def one_star_solution(data):
    zipped_data = list(zip(*data))
    gamma_rate = []
    epsilon_rate = []

    for bit_field in zipped_data:
        total = sum(bit_field)

        if total >= len(bit_field)-total:
            gamma_rate.append(1)
            epsilon_rate.append(0)
        else:
            gamma_rate.append(0)
            epsilon_rate.append(1)
    
    gamma_rate_result = convert_to_int(gamma_rate)
    epsilon_rate_result = convert_to_int(epsilon_rate)

    result = gamma_rate_result * epsilon_rate_result
    return result 

def two_star_solution(data):

    def oxygen_generator_rater(data, position):
        if len(data) == 1:
            return data[0]

        zipped_data = list(zip(*data))
        bit_field = zipped_data[position]
        total = sum(bit_field)

        if total >= len(bit_field)-total:
            most_common = 1
        else:
            most_common = 0
            
        filtered = [data_field 
                    for data_field in data 
                    if data_field[position] == most_common]
                        
        return oxygen_generator_rater(filtered, position+1)
    
    def co2_scrubber_rater(data, position):
        if len(data) == 1:
            return data[0]

        zipped_data = list(zip(*data))
        bit_field = zipped_data[position]
        total = sum(bit_field)

        if total < len(bit_field)-total:
            least_common = 1
        else:
            least_common = 0
        
        filtered = [data_field 
                    for data_field in data 
                    if data_field[position] == least_common]
            
        return co2_scrubber_rater(filtered, position+1)

    oxy = oxygen_generator_rater(data, 0)
    co2 = co2_scrubber_rater(data, 0)
    life_support_rating = convert_to_int(oxy) * convert_to_int(co2)

    return life_support_rating

if __name__ == '__main__':
    data = []
    with open(DATAFILE) as f:
        for line in f:
            data.append(list(map(int, list(line.strip()))))
            
    print("One Star Solution: {}".format(one_star_solution(data)))
    print("Two Star Solution: {}".format(two_star_solution(data)))
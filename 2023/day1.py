def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


def solution_part_1(puzzle_input):
    result = 0
    for line in puzzle_input.split('\n'):
        if len(line) > 0:
            first_numer = 0  # Just for sake of code validity
            last_numer = 0  # Just for sake of code validity
            for letter in line:
                if is_integer(letter):
                    first_numer = int(letter)
                    break
            reverse = line[::-1]
            for letter in reverse:
                if is_integer(letter):
                    last_numer = int(letter)
                    break
            final_number = int(str(first_numer) + str(last_numer))
            result += final_number

    return result


def solution_part_2(puzzle_input):
    result = 0
    for line in puzzle_input.split('\n'):
        if len(line) > 0:
            number_array = []
            substring_line = line
            while len(substring_line) > 0:
                if is_integer(substring_line[0]):
                    number_array.append(int(substring_line[0]))
                elif substring_line[0:3] == 'one':
                    number_array.append(1)
                elif substring_line[0:3] == 'two':
                    number_array.append(2)
                elif substring_line[0:5] == 'three':
                    number_array.append(3)
                elif substring_line[0:4] == 'four':
                    number_array.append(4)
                elif substring_line[0:4] == 'five':
                    number_array.append(5)
                elif substring_line[0:3] == 'six':
                    number_array.append(6)
                elif substring_line[0:5] == 'seven':
                    number_array.append(7)
                elif substring_line[0:5] == 'eight':
                    number_array.append(8)
                elif substring_line[0:4] == 'nine':
                    number_array.append(9)

                substring_line = substring_line[1:len(substring_line)]

            final_number = int(str(number_array[0]) + str(number_array[-1]))
            result += final_number

    return result


print('\n--- Part One ---\n')

with open('fixtures/kilenias/1.txt') as file:
    print(f"Kilenias: {solution_part_1(file.read())}")

with open('fixtures/buccaneer/1.txt') as file:
    print('Buccaneer: ' + str(solution_part_1(file.read())))

print('\n--- Part Two ---\n')

with open('fixtures/kilenias/1.txt') as file:
    print(f"Kilenias: {solution_part_2(file.read())}")

with open('fixtures/buccaneer/1.txt') as file:
    print('Buccaneer: ' + str(solution_part_2(file.read())))

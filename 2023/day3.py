import re
import numpy


def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


def find_symbol(riddle):
    dot_comp = re.compile('[^.]')
    finder = dot_comp.findall(riddle)
    for item in finder:
        if item != '\n':
            if not is_integer(item):
                return True


def find_coordinates_of_symbols(puzzle):
    symbol_array = []
    line_number = 0
    for lines in puzzle.split('\n'):
        character_number = 0
        for character in lines:
            if find_symbol(character):
                symbol_array.append(f'{line_number}, {character_number}')
            character_number += 1
        line_number += 1
    return symbol_array


def num_coord_finder(puzzle):
    comp = re.compile('\d{1,3}')
    finder = comp.finditer(puzzle)
    return finder


def symbol_coord_finder(puzzle):
    digit_comp = re.compile('\W')
    digit_finder = digit_comp.finditer(puzzle)
    return digit_finder


def match_array(line, column, number_array, old_match):
    if line >= 0:
        if column >= 0:
            if number_array[line][column] > 0:
                match = number_array[line][column]
                if match != old_match:
                    return match

    return 0


def get_number_array(puzzle_input):
    line_num = 0
    number_array = numpy.zeros([140, 140], dtype=int)
    for line in puzzle_input.split('\n'):
        for i in num_coord_finder(line):
            j = i.start()
            while j < i.end():
                number_array[line_num][j] = i.group()
                j += 1
        line_num += 1

    return number_array


def solution_part_1(puzzle_input):
    result = 0
    number_array = get_number_array(puzzle_input)

    line_num = 0
    for line in puzzle_input.split('\n'):
        for i in symbol_coord_finder(line):
            if i.group() != '.':
                old_match = 0
                for lines in {line_num - 1, line_num, line_num + 1}:
                    for columns in {i.start() - 1, i.start(), i.start() + 1}:
                        if lines == line_num and columns == i.start():
                            continue
                        else:
                            match = match_array(lines, columns, number_array, old_match)
                            if match > 0:
                                old_match = match
                                result += match

        line_num += 1

    return result


def solution_part_2(puzzle_input):
    result = 0
    number_array = get_number_array(puzzle_input)

    line_num = 0
    for line in puzzle_input.split('\n'):
        for i in symbol_coord_finder(line):
            if i.group() == '*':
                old_match = 0
                match_dict = {}
                counter = 0
                for lines in {line_num - 1, line_num, line_num + 1}:
                    for columns in {i.start() - 1, i.start(), i.start() + 1}:
                        if lines == line_num and columns == i.start():
                            continue
                        else:
                            match = match_array(lines, columns, number_array, old_match)
                            if match > 0:
                                old_match = match
                                match_dict[counter] = match
                                counter += 1

                if counter == 2:
                    result += match_dict[0] * match_dict[1]

        line_num += 1

    return result


print('\n--- Part One ---\n')

with open('fixtures/kilenias/3.txt') as file:
    print(f"Kilenias: {solution_part_1(file.read())}")

with open('fixtures/buccaneer/3.txt') as file:
    print('Buccaneer: ' + str(solution_part_1(file.read())))

print('\n--- Part Two ---\n')

with open('fixtures/kilenias/3.txt') as file:
    print(f"Kilenias: {solution_part_2(file.read())}")

with open('fixtures/buccaneer/3.txt') as file:
    print('Buccaneer: ' + str(solution_part_2(file.read())))

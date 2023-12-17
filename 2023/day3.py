import re


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
    symbol_list = []
    for item in finder:
        if item != '\n':
            if not is_integer(item):
                return True
                # symbol_list.append(item)
    # return symbol_list


def find_coordinates_of_symbols(puzzle):
    symbol_array = []
    line_number = 0
    for lines in puzzle.split('\n'):
        character_number = 0
        for character in lines:
            if find_symbol(character):
                # print(str(line_number) + ',' + str(character_number))
                symbol_array.append(f'{line_number}, {character_number}')
            character_number += 1
        line_number += 1
    return symbol_array


def get_numbers_by_coordinates(puzzle):
    number = False
    numbers = []
    line_number = 0
    numbers_index = 0
    for lines in puzzle.split('\n'):
        character_number = 0
        for character in lines:
            dot_comp = re.compile('[0-9]')
            finder = dot_comp.findall(character)
            if len(finder) > 0:
                try:
                    numbers[numbers_index - 1] = numbers[numbers_index - 1] + character
                    number = True

                except IndexError:
                    number = False
                    # ignore

                try:
                    if number:
                        numbers[numbers_index - 2] = numbers[numbers_index - 2] + character

                except IndexError:
                    number = False
                    # ignore

                numbers[numbers_index] = (f'{line_number},{character_number}:{character}')
                number = True
            else:
                number = False
            numbers_index += 1
            character_number += 1
    return numbers


def num_coord_finder_test(puzzle):
    two_digit_comp = re.compile('\d{2,3}')
    # three_digit_comp = re.compile('\d\d\d')
    two_digit_finder = two_digit_comp.finditer(puzzle)
    # three_digit_finder = three_digit_comp.search(puzzle)
    return two_digit_finder  # , three_digit_finder


#with open('fixtures/buccaneer/3.txt') as file:
#    puzzle_input = file.read()
#    print(get_numbers_by_coordinates(puzzle_input))

with open('fixtures/kilenias/3.txt', 'r') as file:
    puzzle_input = file.read()
    # print(find_coordinates_of_symbols(puzzle_input_kilenias))
    line_num = 0
    number_dict = {}
    for line in puzzle_input.split('\n'):

        # print(line)
        for i in num_coord_finder_test(line):
            number_dict[f'{line_num} {i.span()}'] = i.group()
            # print(i)
        line_num += 1
    print(number_dict)

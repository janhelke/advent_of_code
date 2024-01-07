def card_lister(line):
    winning_numbers = line.split(":")[1].split("|")[0].split(" ")
    your_numbers = line.split(":")[1].split("|")[1].split(" ")
    return winning_numbers, your_numbers


def solution_part_1(puzzle_input):
    result = 0
    for line in puzzle_input.split('\n'):
        points = 0
        split_card = card_lister(line)
        for i in split_card[0]:
            if i != "":
                if i in split_card[1]:
                    if points == 0:
                        points += 1
                    else:
                        points *= 2
        result += points
    return result


def solution_part_2(puzzle_input):
    result = 0
    scratchcard_dict = {}
    counter = 1
    for line in puzzle_input.split('\n'):
        scratchcard_dict[counter] = 1
        counter += 1

    counter = 1
    for line in puzzle_input.split('\n'):
        matches = 0
        split_card = card_lister(line)
        for i in split_card[0]:
            if i != "":
                if i in split_card[1]:
                    matches += 1
        i = 1
        while i <= matches:
            scratchcard_dict[counter + i] += scratchcard_dict[counter]
            i += 1

        counter += 1

    for scratchcard in scratchcard_dict:
        result += scratchcard_dict[scratchcard]
    return result


print('\n--- Part One ---\n')

with open('fixtures/advent_of_code/4.txt') as file:
    reference_result = solution_part_1(file.read())
    if reference_result == 13:
        with open('fixtures/kilenias/4.txt') as file:
            print(f"Kilenias: {solution_part_1(file.read())}")

        with open('fixtures/buccaneer/4.txt') as file:
            print('Buccaneer: ' + str(solution_part_1(file.read())))
    else:
        print(f"Advent of code: {reference_result}")

print('\n--- Part Two ---\n')

with open('fixtures/advent_of_code/4.txt') as file:
    reference_result = solution_part_2(file.read())
    if reference_result == 30:
        with open('fixtures/kilenias/4.txt') as file:
            print(f"Kilenias: {solution_part_2(file.read())}")

        with open('fixtures/buccaneer/4.txt') as file:
            print('Buccaneer: ' + str(solution_part_2(file.read())))
    else:
        print(f"Advent of code: {reference_result}")

def solution_part_1(puzzle_input):
    floor = 0
    for character in puzzle_input:
        if character == '(':
            floor += 1
        if character == ')':
            floor -= 1

    return floor


def solution_part_2(puzzle_input):
    floor = 0
    counter = 0
    for character in puzzle_input:
        counter += 1
        if character == '(':
            floor += 1
        if character == ')':
            floor -= 1

        if floor == -1:
            return counter


print('\n--- Part One ---\n')

with open('fixtures/buccaneer/1.txt') as file:
    print('Buccaneer: ' + str(solution_part_1(file.read())))

print('\n--- Part Two ---\n')

with open('fixtures/buccaneer/1.txt') as file:
    print('Buccaneer: ' + str(solution_part_2(file.read())))
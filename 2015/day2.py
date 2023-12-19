def solution_part_1(puzzle_input):
    result = 0
    for line in puzzle_input.split('\n'):
        surface = 0
        full_surface = 0
        length, width, height = list(map(int,line.split('x')))
        surface = length * width
        full_surface += 2 * surface
        smalles_surface = surface
        surface = height * width
        full_surface += 2 * surface
        if surface < smalles_surface:
            smalles_surface = surface
        surface = length * height
        full_surface += 2 * surface
        if surface < smalles_surface:
            smalles_surface = surface
        full_surface += smalles_surface
        result += full_surface

    return result


def solution_part_2(puzzle_input):
    result = 0
    for line in puzzle_input.split('\n'):
        dimensions = list(map(int,line.split('x')))
        dimensions.sort()
        ribbon = 2 * dimensions[0] + 2 * dimensions[1] + dimensions[0] * dimensions[1] * dimensions[2]
        result += ribbon

    return result




print('\n--- Part One ---\n')

with open('fixtures/buccaneer/2.txt') as file:
    print('Buccaneer: ' + str(solution_part_1(file.read())))

print('\n--- Part Two ---\n')

with open('fixtures/buccaneer/2.txt') as file:
    print('Buccaneer: ' + str(solution_part_2(file.read())))
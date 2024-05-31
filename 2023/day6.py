from pprint import pprint

def race(time, max_distance):
    won_races = 0
    timer = 0
    while timer <= time:
        distance_sailed = timer * (time - timer)
        if max_distance < distance_sailed:
            #won_races += 1
            return (time + 1 - (2 * timer))
        timer += 1
    return won_races


def solution_part_1(puzzle_input):
    result = 1
    lines = puzzle_input.split('\n')
    times = lines[0].split()
    max_distances = lines[1].split()

    result *= race(int(times[1]), int(max_distances[1]))
    result *= race(int(times[2]), int(max_distances[2]))
    result *= race(int(times[3]), int(max_distances[3]))
    try:
        if times[4]:
            result *= race(int(times[4]), int(max_distances[4]))
    except IndexError:
        print ('')

    return result


def solution_part_2(puzzle_input):
    result = 0
    result = 1
    lines = puzzle_input.split('\n')
    times = lines[0].split()
    max_distances = lines[1].split()

    try:
        if times[4]:
            result = race(int(times[1]+times[2]+times[3]+times[4]), int(max_distances[1]+max_distances[2]+max_distances[3]+max_distances[4]))
    except IndexError:
        result = race(int(times[1] + times[2] + times[3]),
                      int(max_distances[1] + max_distances[2] + max_distances[3]))

    return result


print('\n--- Part One ---\n')

with open('fixtures/advent_of_code/6.txt') as file:
    reference_result = solution_part_1(file.read())
    if reference_result == 288:
        with open('fixtures/kilenias/6.txt') as file:
            print(f"Kilenias: {solution_part_1(file.read())}")

        with open('fixtures/buccaneer/6.txt') as file:
            print('Buccaneer: ' + str(solution_part_1(file.read())))
    else:
        print(f"Advent of code: {reference_result}")

print('\n--- Part Two ---\n')

with open('fixtures/advent_of_code/6.txt') as file:
    reference_result = solution_part_2(file.read())
    if reference_result == 71503:
        with open('fixtures/kilenias/6.txt') as file:
            print(f"Kilenias: {solution_part_2(file.read())}")

        with open('fixtures/buccaneer/6.txt') as file:
            print('Buccaneer: ' + str(solution_part_2(file.read())))
    else:
        print(f"Advent of code: {reference_result}")

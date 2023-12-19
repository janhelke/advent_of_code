def solution_part_1(puzzle_input):
    house = {}
    x = 0
    y = 0
    if x not in house:
        house[x] = {}
    if y not in house[x]:
        house[x][y] = 1

    house[x][y] = 1
    for line in puzzle_input.split('\n'):
        for direction in line:
            if direction == '>':
                x += 1
            if direction == 'v':
                y += 1
            if direction == '<':
                x -= 1
            if direction == '^':
                y -= 1

            if x not in house:
                house[x] = {}
            if y not in house[x]:
                house[x][y] = 0

            house[x][y] += 1

    return sum(len(v) for v in house.values())


def solution_part_2(puzzle_input):
    house = {}
    santa_x = 0
    santa_y = 0
    if santa_x not in house:
        house[santa_x] = {}
    if santa_y not in house[santa_x]:
        house[santa_x][santa_y] = 1
    robo_santa_x = 0
    robo_santa_y = 0
    if robo_santa_x not in house:
        house[robo_santa_x] = {}
    if robo_santa_y not in house[robo_santa_x]:
        house[robo_santa_x][robo_santa_y] += 1

    is_santas_turn = True
    for line in puzzle_input.split('\n'):
        for direction in line:
            if is_santas_turn:
                if direction == '>':
                    santa_x += 1
                if direction == 'v':
                    santa_y += 1
                if direction == '<':
                    santa_x -= 1
                if direction == '^':
                    santa_y -= 1

                if santa_x not in house:
                    house[santa_x] = {}
                if santa_y not in house[santa_x]:
                    house[santa_x][santa_y] = 0

                house[santa_x][santa_y] += 1
                is_santas_turn = False
            else:
                if direction == '>':
                    robo_santa_x += 1
                if direction == 'v':
                    robo_santa_y += 1
                if direction == '<':
                    robo_santa_x -= 1
                if direction == '^':
                    robo_santa_y -= 1

                if robo_santa_x not in house:
                    house[robo_santa_x] = {}
                if robo_santa_y not in house[robo_santa_x]:
                    house[robo_santa_x][robo_santa_y] = 0

                house[robo_santa_x][robo_santa_y] += 1
                is_santas_turn = True

    return sum(len(v) for v in house.values())


print('\n--- Part One ---\n')

with open('fixtures/buccaneer/3.txt') as file:
    print('Buccaneer: ' + str(solution_part_1(file.read())))

print('\n--- Part Two ---\n')

with open('fixtures/buccaneer/3.txt') as file:
    print('Buccaneer: ' + str(solution_part_2(file.read())))

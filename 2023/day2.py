def solution_part_1(puzzle_input):
    bag_of_cubes = {'red': 12, 'green': 13, 'blue': 14}
    result = 0
    for game in puzzle_input.split('\n'):
        if len(game) > 0:
            game_key, drawings_string = game.split(': ')
            game_id = int(game_key.split(' ')[1])
            drawings = drawings_string.split('; ')
            valid_game = True
            for drawing in drawings:
                groups_of_cubes = drawing.split(', ')
                red = 0
                green = 0
                blue = 0
                for group in groups_of_cubes:
                    amount_of_cubes, color = group.split(' ', 2)
                    if color == 'red':
                        red = int(amount_of_cubes)
                    if color == 'green':
                        green = int(amount_of_cubes)
                    if color == 'blue':
                        blue = int(amount_of_cubes)
                if red > bag_of_cubes['red'] or green > bag_of_cubes['green'] or blue > bag_of_cubes['blue']:
                    valid_game = False
            if valid_game:
                result += game_id

    return result


def solution_part_2(puzzle_input):
    result = 0
    for game in puzzle_input.split('\n'):
        if len(game) > 0:
            game_key, drawings_string = game.split(': ')
            drawings = drawings_string.split('; ')
            red_list = []
            green_list = []
            blue_list = []
            for drawing in drawings:
                groups_of_cubes = drawing.split(', ')
                for cube in groups_of_cubes:
                    amount_of_cubes, color = cube.split(' ')
                    if color == 'red':
                        red_list.append(int(amount_of_cubes))
                    if color == 'green':
                        green_list.append(int(amount_of_cubes))
                    if color == 'blue':
                        blue_list.append(int(amount_of_cubes))
            result += max(red_list) * max(green_list) * max(blue_list)

    return result


print('\n--- Part One ---\n')

with open('fixtures/kilenias/2.txt') as file:
    print(f"Kilenias: {solution_part_1(file.read())}")

with open('fixtures/buccaneer/2.txt') as file:
    print('Buccaneer: ' + str(solution_part_1(file.read())))

print('\n--- Part Two ---\n')

with open('fixtures/kilenias/2.txt') as file:
    print(f"Kilenias: {solution_part_2(file.read())}")

with open('fixtures/buccaneer/2.txt') as file:
    print('Buccaneer: ' + str(solution_part_2(file.read())))

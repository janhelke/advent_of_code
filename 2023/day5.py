def map_value(seed_dict, line):
    mapped_value = {}
    for seed in seed_dict:
        mapped_value[seed] = seed
        destination_range_start, source_range_start, range_length = line.split(' ')
        if seed in range(int(source_range_start), int(source_range_start) + int(range_length)):
            mapped_value[seed] = int(destination_range_start) - int(source_range_start) + seed

    return mapped_value


def solution_part_1(puzzle_input):
    result = 0
    seed_to_soil = {}
    soil_to_fertilizer = {}
    fertilizer_to_water = {}
    water_to_light = {}
    light_to_temperature = {}
    temperature_to_humidity = {}
    humidity_to_location = {}
    max_number = 99
    action = ''

    seed_dict = {79, 14, 55, 13}

    for line in puzzle_input.split('\n'):

        if line == 'seed-to-soil map:':
            action = 'seed-to-soil'
        elif line == 'soil-to-fertilizer map:':
            action = 'soil-to-fertilizer'
        elif line == 'fertilizer-to-water map:':
            action = 'fertilizer-to-water'
        elif line == 'water-to-light map:':
            action = 'water-to-light'

        elif line == 'light-to-temperature map:':
            action = 'light-to-temperature'

        elif line == 'temperature-to-humidity map:':
            action = 'temperature-to-humidity'

        elif line == 'humidity-to-location map:':
            action = 'humidity-to-location'

        elif line == '':
            action = ''

        else:
            if action == 'seed-to-soil':
                seed_to_soil = map_value(seed_dict, line)
            elif action == 'soil-to-fertilizer':
                soil_to_fertilizer = map_value(seed_dict, line)
            elif action == 'fertilizer-to-water':
                fertilizer_to_water = map_value(seed_dict, line)
            elif action == 'water-to-light':
                water_to_light = map_value(seed_dict, line)
            elif action == 'light-to-temperature':
                light_to_temperature = map_value(seed_dict, line)
            elif action == 'temperature-to-humidity':
                temperature_to_humidity = map_value(seed_dict, line)
            elif action == 'humidity-to-location':
                humidity_to_location = map_value(seed_dict, line)
            else:
                continue

    print(seed_to_soil)
    print(soil_to_fertilizer)
    print(fertilizer_to_water)
    print(water_to_light)
    print(light_to_temperature)
    print(temperature_to_humidity)
    print(humidity_to_location)

    return result


def solution_part_2(puzzle_input):
    result = 0

    return result


print('\n--- Part One ---\n')

with open('fixtures/advent_of_code/5.txt') as file:
    reference_result = solution_part_1(file.read())
    if reference_result == 35:
        with open('fixtures/kilenias/5.txt') as file:
            print(f"Kilenias: {solution_part_1(file.read())}")

        with open('fixtures/buccaneer/5.txt') as file:
            print('Buccaneer: ' + str(solution_part_1(file.read())))
    else:
        print(f"Advent of code: {reference_result}")

print('\n--- Part Two ---\n')

with open('fixtures/advent_of_code/5.txt') as file:
    reference_result = solution_part_2(file.read())
    if reference_result == 999:
        with open('fixtures/kilenias/5.txt') as file:
            print(f"Kilenias: {solution_part_2(file.read())}")

        with open('fixtures/buccaneer/5.txt') as file:
            print('Buccaneer: ' + str(solution_part_2(file.read())))
    else:
        print(f"Advent of code: {reference_result}")

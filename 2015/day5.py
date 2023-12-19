import re


def solution_part_1(puzzle_input):
    nice_strings = 0
    for line in puzzle_input.split('\n'):
        last_character = ''
        vowels = 0
        twice = False
        if (not re.search('(ab)', line)
                and not re.search('(cd)', line)
                and not re.search('(pq)', line)
                and not re.search('(xy)', line)
        ):
            for character in line:
                if re.search('[aeiou]', character):
                    vowels += 1
                if last_character == character:
                    twice = True

                last_character = character

            if vowels >= 3 and twice:
                nice_strings += 1

    return nice_strings


def solution_part_2(puzzle_input):
    nice_strings = 0
    for line in puzzle_input.split('\n'):
        tupels = 0
        
    return nice_strings


print('\n--- Part One ---\n')

with open('fixtures/buccaneer/5.txt') as file:
    print('Buccaneer: ' + str(solution_part_1(file.read())))

print('\n--- Part Two ---\n')

with open('fixtures/buccaneer/5.txt') as file:
    print('Buccaneer: ' + str(solution_part_2(file.read())))

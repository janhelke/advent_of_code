import hashlib


def solution_part_1(puzzle_input):
    iterator = 0
    while True:
        hashing_value = hashlib.md5((puzzle_input + str(iterator)).encode())
        if hashing_value.hexdigest()[0:5] == '00000':
            break
        iterator += 1

    return iterator


def solution_part_2(puzzle_input):
    iterator = 0
    while True:
        hashing_value = hashlib.md5((puzzle_input + str(iterator)).encode())
        if hashing_value.hexdigest()[0:6] == '000000':
            break
        iterator += 1

    return iterator


print('\n--- Part One ---\n')

with open('fixtures/buccaneer/4.txt') as file:
    print('Buccaneer: ' + str(solution_part_1(file.read())))

print('\n--- Part Two ---\n')

with open('fixtures/buccaneer/4.txt') as file:
    print('Buccaneer: ' + str(solution_part_2(file.read())))

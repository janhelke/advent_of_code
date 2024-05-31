from pprint import pprint

def rank_hands(hands_list):
    ranking = []
    hands_with_bets = {}
    multiplier = len(hands_list)
    winnings = 0

    for hand in hands_list:
        hand_dict = {}
        hands_with_bets[hand.split()[0]] = hand.split()[1]
        for card in hand.split()[0]:
            if hand_dict.get(card) is None:
                hand_dict[card] = 1
            else:
                hand_dict[card] += 1
        rank = 1
        for card, amount in hand_dict.items():
            if amount == 2:
                if rank == 2:
                    rank = 3
                elif rank == 4:
                    rank = 5
                else:
                    rank = 2
            if amount == 3:
                if rank == 2:
                    rank = 5
                else:
                    rank = 4
            if amount == 4:
                rank = 6
            if amount == 5:
                rank = 7

        ranking.append(str(rank) + hand.split()[0])

    alphabet = 'AKQJT987654321'
    new_ranking = sorted(ranking, key=lambda word: [alphabet.index(c) for c in word])
    for position in new_ranking:
        winnings += int(hands_with_bets.get(position[1:6])) * multiplier
        multiplier -= 1

    return winnings


def solution_part_1(puzzle_input):
    result = rank_hands(puzzle_input.split('\n'))
    return result


def solution_part_2(puzzle_input):
    result = 0

    return result


print('\n--- Part One ---\n')

with open('fixtures/advent_of_code/7.txt') as file:
    reference_result = solution_part_1(file.read())
    if reference_result == 6440:
        with open('fixtures/kilenias/7.txt') as file:
            print(f"Kilenias: {solution_part_1(file.read())}")

        with open('fixtures/buccaneer/7.txt') as file:
            print('Buccaneer: ' + str(solution_part_1(file.read())))
    else:
        print(f"Advent of code: {reference_result}")

print('\n--- Part Two ---\n')

with open('fixtures/advent_of_code/7.txt') as file:
    reference_result = solution_part_2(file.read())
    if reference_result == 71503:
        with open('fixtures/kilenias/7.txt') as file:
            print(f"Kilenias: {solution_part_2(file.read())}")

        with open('fixtures/buccaneer/7.txt') as file:
            print('Buccaneer: ' + str(solution_part_2(file.read())))
    else:
        print(f"Advent of code: {reference_result}")

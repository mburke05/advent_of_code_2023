from collections import deque


def read_file():
    with open("input.txt", "r") as f:
        lines = f.readlines()
    return lines


"""
part 1 code. simple parsing of the input file and then checking for winning numbers.
"""
# # winning_card_scores = 0
# for card in read_file():
#     print(card)
#     winning_number_count = 0
#     numbers = [
#         [int(num) for num in group.split() if num]
#         for group in card.split(":")[1].split("|")
#     ]

#     for num in numbers[1]:
#         if num in numbers[0]:
#             print("Found a winning number: ", num)
#             winning_number_count += 1
#     if winning_number_count > 0:
#         print("Winning number count: ", winning_number_count)
#         winning_card_scores += 2 ** (winning_number_count - 1)

# # part 1
# print("Total score: ", winning_card_scores)

###
# part 2 using a queue


def card_score_counts(cards):
    card_points = {}
    for idx, card in enumerate(cards):
        winning_number_count = 0
        numbers = [
            [int(num) for num in group.split() if num]
            for group in card.split(":")[1].split("|")
        ]

        for num in numbers[1]:
            if num in numbers[0]:
                winning_number_count += 1
        card_points[idx] = winning_number_count

    return card_points


def count_total_scratchcards(scratchcards):
    queue = deque(scratchcards)

    total_scratchcards = 0

    while queue:
        card_number, matching_numbers = queue.popleft()
        total_scratchcards += 1

        for _ in range(matching_numbers):
            queue.append(scratchcards[card_number + _ + 1])

    return total_scratchcards


cards = read_file()
hash_table = card_score_counts(cards)

scratchcards = [(card_number, hash_table[card_number]) for card_number in hash_table]

total_scratchcards = count_total_scratchcards(scratchcards)

print(total_scratchcards)
